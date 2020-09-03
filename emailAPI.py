import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from emailPipeline import *

# sender's email should be Gmail
def sendEmail(email_data, session):
    sender = email_data["sender"] # e.g., "cpark@powersimtech.com"
    password = email_data["password"] # e.g., "chansunPower95"
    recipient = email_data["recipient"] # e.g., "chansun@live.unc.edu"
    cc = email_data["cc"] # e.g., ['chansun95@gmail.com', "findchansun1995@gmail.com"]
    bcc = email_data["bcc"] # ["8027715@bcc.hubspot.com"]
    reply_to = email_data["reply_to"] # e.g., "sales@powersimtech.com"
    subject = email_data["subject"] # .e.g., "PSIM Quote 123456789"
    quote_email_template = email_data["quote_email_template"] # e.g., "under_5000"
    addressee = email_data["addressee"] # e.g., "Chansun Park"
    sign_off = email_data["sign_off"] # e.g., "Tricia"
    pdf_file_name = email_data["pdf_file_name"] # e.g., PSIM Quote # - Company_name (v.#)
    mail_content_html = createEmailTemplateUnder5000(addressee, sign_off) if quote_email_template == "under_5000" else createEmailTemplateOver5000(addressee, sign_off)

    msg = MIMEMultipart()    
    msg['From'] = sender
    msg['To'] = recipient
    if len(cc) >= 1:
        msg['Cc'] = ",".join(cc)
    msg['Subject'] = subject
    msg['Reply-to'] = reply_to
    msg.attach(MIMEText(mail_content_html, 'html'))

    path_to_pdf = "./pdfs/{0}.pdf".format(pdf_file_name)
    with open(path_to_pdf, "rb") as f:
        attach = MIMEApplication(f.read(),_subtype="pdf")
    attach.add_header('Content-Disposition','attachment',filename=str(pdf_file_name)+".pdf")
    msg.attach(attach)
    '''
    session = smtplib.SMTP('smtp.gmail.com', 587) # Gmail port : 587
    session.starttls() # Enable security
    session.login(sender, password)
    '''
    if len(cc) >= 1:
        session.sendmail(sender, [recipient] + cc + bcc, msg.as_string())
    else:
        session.sendmail(sender, [recipient] + bcc, msg.as_string())
    session.quit()
    print('Mail Sent')