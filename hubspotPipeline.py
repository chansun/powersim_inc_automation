from hubspotAPI import *
import datetime
import time
import asyncio
import functools
from googleAPI import getCurrentQuoteVersion

# Input: None
# Output: Dictionary where keys are "mon", "day", or "year" and values are today's month, day, and year.
# ============================ Example ============================
# >>> getDate()
# {'mon': 'August', 'day': '8', 'year': '2020'}
# ============================ Example ============================
def getDate():
    current_time = datetime.datetime.now()
    return {"mon": str(current_time.strftime("%B")), "day": str(current_time.day), "year": str(current_time.year)}

# Input: Deal object
# Output: Value of "quote_prepared_by_" property; the name of the quote preparer; None if there is no value assigned to the property
# ============================ Example ============================
# >>> getPreparerByDealObject(deal_object1)
# None
# >>> getPreparerByDealObject(deal_object2)
# 'Shannon Chesley'
# ============================ Example ============================
def getPreparerByDealObject(deal_object):
    return deal_object["properties"]["quote_prepared_by_"]

# Input: Deal object
# Output: Next quote version
# ============================ Example ============================
# >>> getQuoteVersion(deal_object1)
# '1'
# >>> getQuoteVersion(deal_object2)
# '2'
# ============================ Example ============================
async def getQuoteVersion(deal_object):
    url_drive_quote = deal_object["properties"]["url_drive_quote"]
    if url_drive_quote == None or url_drive_quote.strip() == "":
        return str(1)
    else:
        return str(int(await getCurrentQuoteVersion(url_drive_quote)) + 1)

# Input: Contact object
# Output: Person name associated with the contact object
# ============================ Example ============================
# >>> getNameByContactObject(contact_object)
# 'Chansun Park'
# ============================ Example ============================
def getNameByContactObject(contact_object):
    return contact_object["properties"]["firstname"] + " " + contact_object["properties"]["lastname"]

# Input: Contact object
# Output: Contact object ID
# ============================ Example ============================
# >>> getIdByContactObject(contact_object)
# '123456789'
# ============================ Example ============================
def getIdByContactObject(contact_object):
    return contact_object["id"]

# Input: Contact object
# Output: Name of country associated with the contact object
# ============================ Example ============================
# >>> getCountryByContactObject(contact_object)
# 'Singapore'
# ============================ Example ============================
def getCountryByContactObject(contact_object):
    return contact_object["properties"]["country"]

# Input: Company object
# Output: Company name
# ============================ Example ============================
# >>> getNameByCompanyObject(company_object)
# 'FITSUM'
# ============================ Example ============================
def getNameByCompanyObject(company_object):
    return company_object["properties"]["name"]

# Input: a list of contact objects, contact Id.
# Output: Contact object
# ============================ Example ============================
# >>> selectContactObject(contact_objects, selected_contact_id)
# {'id': '43047101', 'properties': {'address': None, 'city': None, 'company': 'FITSUM', 'country': 'Australia', ...}, ...}
# ============================ Example ============================
def selectContactObject(contact_objects, selected_contact_id):
    for contact_object in contact_objects:
        if str(selected_contact_id) == str(contact_object["id"]):
            selected_contact_object = contact_object
            return selected_contact_object

# Input: Deal Id
# Output: Dictionary that contains 1. deal object, 2. contact objects, 3. company object, 4. quote version
# ============================ Example ============================
# >>> getData("2377191492")
# {"deal_object": deal_object, "contact_objects": contact_objects, "company_object": company_object, "quote_version": quote_version}
# ============================ Example ============================
async def getData(deal_id):
    futures = [asyncio.ensure_future(getDeal(deal_id)), 
               asyncio.ensure_future(getAssociatedContactIds(deal_id)),
               asyncio.ensure_future(getAssociatedCompanyId(deal_id))
              ]
    results = await asyncio.gather(*futures)
    deal_object = results[0]
    contact_ids = results[1] # array
    company_id = results[2] # string
    futures2 = [asyncio.ensure_future(getContact(str(contact_id))) for contact_id in contact_ids]
    results2 = await asyncio.gather(*futures2)
    contact_objects = results2
    futures3 = [asyncio.ensure_future(getCompany(company_id)), asyncio.ensure_future(getQuoteVersion(deal_object))]    
    results3 = await asyncio.gather(*futures3)
    company_object = results3[0]
    quote_version = results3[1]
    data = {
        "deal_object": deal_object,
        "contact_objects": contact_objects,
        "company_object": company_object,
        "quote_version": quote_version
    }
    return data

# Input: Contact objects
# Output: Dictionary where keys are contact ids and values are strings containing name, country, and contact id information associated with each contact object
# ============================ Example ============================
# >>> getContactList(contact_objects)
# {'12345': "Name: Chansun Park // Country: USA // Contact ID: 99999999", '67890': "Name: James Lee // Country: Germany // Contact ID: 8888888"}
# ============================ Example ============================
def getContactList(contact_objects):
    contact_list = {} # {id: "Name: Chansun Park // Country: USA // Contact ID: 99999999"}
    for contact_object in contact_objects:
        contact_list[getIdByContactObject(contact_object)] = ""
        contact_list[getIdByContactObject(contact_object)] += "Name: {0}".format(getNameByContactObject(contact_object))
        contact_list[getIdByContactObject(contact_object)] += " // "
        contact_list[getIdByContactObject(contact_object)] += "Country: {0}".format(getCountryByContactObject(contact_object))
        #contact_list[getIdByContactObject(contact_object)] += " // "
        #contact_list[getIdByContactObject(contact_object)] += "Contact ID: {0}".format(getIdByContactObject(contact_object))
    return contact_list

# Input: Data, contact id
# Output: Data needed for quote header
# ============================ Example ============================
# >>> getHeaderData(data, selected_contact_id)
# header_data = {"quote_version": quote_version, "preparer_name": preparer_name, "quote_number": quote_number, "mon": date["mon"], "day": date["day"], "year": date["year"], "prepared_for": prepared_for, "company_name": company_name, "country_or_region": country_or_region}
# ============================ Example ============================
def getHeaderData(data, selected_contact_id):
    quote_version = data["quote_version"]
    deal_object = data["deal_object"]
    #prepared_by = getPreparerByDealObject(deal_object)
    #preparer_name = "Shannon Chesley" if (prepared_by == None or prepared_by == "") else prepared_by # Default is Shannon Chesley; 
    deal_id = deal_object["id"]
    quote_number = str(deal_id)
    date = getDate()
    contact_objects = data["contact_objects"]
    selected_contact_object = selectContactObject(contact_objects, selected_contact_id)
    prepared_for = getNameByContactObject(selected_contact_object)
    company_object = data["company_object"]
    company_name = getNameByCompanyObject(company_object)
    country_or_region = getCountryByContactObject(selected_contact_object)
    header_data = {
        "quote_version": quote_version, 
        #"preparer_name": preparer_name,
        "quote_number": quote_number,
        "mon": date["mon"],
        "day": date["day"],
        "year": date["year"],
        "prepared_for": prepared_for,
        "company_name": company_name, 
        "country_or_region": country_or_region
    }
    return header_data