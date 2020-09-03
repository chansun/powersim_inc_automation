from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import io
from apiclient.http import MediaIoBaseDownload
from hubspotAPI import loop
import asyncio
import functools
import time

SCOPES = ['https://www.googleapis.com/auth/documents', 'https://www.googleapis.com/auth/drive']
creds = None
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)
        
service_docs = build('docs', 'v1', credentials=creds)
service_drive = build('drive', 'v2', credentials=creds)

# Input: Link to google docs quote
# Output: Current quote version
# ============================ Example ============================
# >>> link = 'https://docs.google.com/document/d/1JHBrlCUaSoarFwtlSzSdsGgy3NK_PQ5lxREK_-L9QaQ/edit#'
# >>> getCurrentQuoteVersion(link)
# '2'
# ============================ Example ============================
async def getCurrentQuoteVersion(link):
    docs_id = linkToDocsId(link)
    temp = await loop.run_in_executor(None, functools.partial(service_drive.files().export, fileId=docs_id, mimeType="text/plain"))
    binary_text = temp.execute()    
    q_index = binary_text.find(b'Quote v.')
    version = ""
    for i in range(0, 13):
        if ord(chr(binary_text[i + q_index])) >= ord("0") and ord(chr(binary_text[i + q_index])) <= ord("9"):
            version += chr(binary_text[q_index+i])
    return version

# Input: 1. link of google docs file to be copied, 
# 2. link of the google docs folder where the copy will be stored at,
# 3. title of copy
# Output: link of copy
# ============================ Example ============================
# origin_file_link = "https://docs.google.com/document/d/1H9ysTyQjTzyA0-H8-W2wof7HSA3INNyxHpd5pTBeorE/edit"
# folder_link = "https://drive.google.com/drive/u/0/folders/1k_Qsivs7Db6kPtg74k-SsH_x9zarq-Hd"
# copy_title = "industry"
# >>> makeCopy(origin_file_link, folder_link, copy_title)
# 'https://docs.google.com/document/d/1h_r9vddaPD5NLtkGx9Z3ylJoG4f7UX1k9yF_Kl3USTQ/edit?usp=drivesdk'
# ============================ Example ============================
def makeCopy(origin_file_link, folder_link, copy_title):
    origin_file_id = linkToDocsId(origin_file_link)
    folder_id = linkToDocsId(folder_link)
    copied_file = {'title': copy_title, 'parents': [{'id': folder_id}]}
    try:
        copy = service_drive.files().copy(fileId=origin_file_id, body=copied_file).execute()
        google_docs_link = copy["alternateLink"]
        return google_docs_link
    except(errors.HttpError, error):
        print('An error occurred: %s' % error)
        return None

# Input: Link to google docs template, request data
# Output: Link to google docs template
# ============================ Example ============================
# >>> link = 'https://docs.google.com/document/d/1mZ_W9r-cYIJLX2uC1A4x_IZMuw-QCyQHR3Q569WWLeA/edit'
# >>> requests = makeRequests(header_data)
# >>> populateData(link, requests)
# 'https://docs.google.com/document/d/1mZ_W9r-cYIJLX2uC1A4x_IZMuw-QCyQHR3Q569WWLeA/edit'
# ============================ Example ============================
def populateData(link, requests):
    docs_id = linkToDocsId(link)
    document = service_docs.documents().batchUpdate(documentId=docs_id, body={'requests': requests}).execute()
    return link

# Input: 1. google docs link, 2. file name for the pdf file to be donwloaded
# Output: None
# ============================ Example ============================
# link = "https://docs.google.com/document/d/1zHd5KP7EK1WQ3K_wuuAk27Y2St81ZYvBVXCmdsSIiNk/edit#heading=h.7a9vzqcg994w"
# file_name = "Quote 2377191492 - FITSUM"
# >>> download(link, file_name)
# 0
# ============================ Example ============================
def download(link, file_name):
    docs_id = linkToDocsId(link)
    request = service_drive.files().export_media(fileId=docs_id, mimeType="application/pdf")
    fh = io.FileIO("./pdfs/{0}.pdf".format(file_name), 'wb')
    #fh = io.FileIO("./temp_copies/{0}.pdf".format(file_name), 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
    return 0

# Input: google docs link
# Output: google docs id
# ============================ Example ============================
# link = "https://docs.google.com/document/d/1zHd5KP7EK1WQ3K_wuuAk27Y2St81ZYvBVXCmdsSIiNk/edit#heading=h.7a9vzqcg994w"
# file_name = "Quote 2377191492 - FITSUM"
# >>> linkToDocsId(link)
# '1zHd5KP7EK1WQ3K_wuuAk27Y2St81ZYvBVXCmdsSIiNk'
# ============================ Example ============================
def linkToDocsId(link):
    if link.find("/d/") == -1:
        docs_id = link[link.find("/folders/")+9:]
    else:
        docs_id = link[link.find("/d/")+3:link.find("/edit")]
    return docs_id