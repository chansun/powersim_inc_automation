import requests
import json
import asyncio
import functools

super_api_key = "super admin api key here..." # Super Admin API
test_api_key = "test account api key here..." # Test Account API
#api_key = super_api_key
api_key = test_api_key
headers = {'accept': 'application/json', 'content-type': "application/json"}
querystring = {"archived": "false",
               "hapikey": api_key}
querystring_deal = {"properties": "quote_prepared_by_,url_drive_quote,dealstage", 
                    "archived": "false",
                    "hapikey": api_key}
querystring_contact = {"properties": "firstname,lastname,company,phone,email,address,city,state,zip,country",
                       "archived": "false", 
                       "hapikey": api_key}
querystring_company = {"properties": "name",
                       "archived": "false", 
                       "hapikey": api_key}

loop = asyncio.get_event_loop()

# Input: Deal ID
# Output: HubSpot "Deal" object
# ============================ Example ============================
# >>> getDeal("2377191492")
# {'id': '2377191492', 'properties': {'createdate': '2020-07-06T00:31:01.064Z', 'hs_lastmodifieddate': '2020-08-02T17:39:13.305Z', 'hs_object_id': '2377191492', 'quote_prepared_by_': None}, 'createdAt': '2020-07-06T00:31:01.064Z', 'updatedAt': '2020-08-02T17:39:13.305Z', 'archived': False}
# ============================ Example ============================
async def getDeal(deal_id):
    url = "https://api.hubapi.com/crm/v3/objects/deals/{0}".format(deal_id)
    response = await loop.run_in_executor(None, functools.partial(requests.request, "GET", url, headers=headers, params=querystring_deal)) 
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        raise Exception("Network Error")

# Input: Contact ID
# Output: HubSpot "Contact" object
# ============================ Example ============================
# >>> getContact("43047101")
# {'id': '43047101', 'properties': {'createdate': '2020-07-05T22:56:21.519Z', 'email': 'info@fitsum.com.au', 'firstname': 'Lul', 'hs_object_id': '43047101', 'lastmodifieddate': '2020-07-28T16:16:59.994Z', 'lastname': 'Goshu'}, 'createdAt': '2020-07-05T22:56:21.519Z', 'updatedAt': '2020-07-28T16:16:59.994Z', 'archived': False}
# ============================ Example ============================
async def getContact(contact_id):
    url = "https://api.hubapi.com/crm/v3/objects/contacts/{0}".format(contact_id)
    response = await loop.run_in_executor(None, functools.partial(requests.request, "GET", url, headers=headers, params=querystring_contact))
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        raise Exception("Network Error")

# Input: Company ID
# Output: HubSpot "Company" object
# ============================ Example ============================
# >>> getCompany("4117968100")
# {'id': '4117968100', 'properties': {'createdate': '2020-07-05T22:56:21.848Z', 'domain': 'fitsum.com.au', 'hs_lastmodifieddate': '2020-08-02T17:39:13.306Z', 'hs_object_id': '4117968100', 'name': 'FITSUM'}, 'createdAt': '2020-07-05T22:56:21.848Z', 'updatedAt': '2020-08-02T17:39:13.306Z', 'archived': False}
# ============================ Example ============================
async def getCompany(company_id):
    url = "https://api.hubapi.com/crm/v3/objects/company/{0}".format(company_id)
    response = await loop.run_in_executor(None, functools.partial(requests.request, "GET", url, headers=headers, params=querystring_company))
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        raise Exception("Network Error")

# Input: Deal ID
# Output: Associated "Contact" object's ID
# ============================ Example ============================
# >>> getAssociatedContactId("2377191492")
# '43047101'
# ============================ Example ============================
#async def getAssociatedContactId(deal_id):
async def getAssociatedContactIds(deal_id):
    url = "https://api.hubapi.com/crm-associations/v1/associations/{0}/HUBSPOT_DEFINED/3?hapikey={1}".format(deal_id, api_key)
    response = await loop.run_in_executor(None, functools.partial(requests.request, "GET", url=url))
    if response.status_code == 200:
        response_dict = json.loads(response.text)
        return response_dict["results"]
        #return str(response_dict["results"][0])
    else:
        raise Exception("Network Error")

# Input: Deal ID of HubSpot's "deal" object
# Output: Associated "Company" object's ID
# ============================ Example ============================
# >>> getAssociatedCompanyId("2377191492")
# '4117968100'
# ============================ Example ============================
async def getAssociatedCompanyId(deal_id):
    url = "https://api.hubapi.com/crm-associations/v1/associations/{0}/HUBSPOT_DEFINED/5?hapikey={1}".format(deal_id, api_key)
    response = await loop.run_in_executor(None, functools.partial(requests.request, "GET", url=url))
    if response.status_code == 200:
        response_dict = json.loads(response.text)
        return str(response_dict["results"][0])
    else:
        raise Exception("Network Error")

'''
async def getAssociatedEngagementId(deal_id):
    url = "https://api.hubapi.com/crm-associations/v1/associations/{0}/HUBSPOT_DEFINED/11?hapikey={1}".format(deal_id, api_key)
    response = await loop.run_in_executor(None, functools.partial(requests.request, "GET", url=url))
    if response.status_code == 200:
        response_dict = json.loads(response.text)
        return str(response_dict["results"][0])
    else:
        raise Exception("Network Error")
'''

# Input: Object type
# Output: All properties of the object type   
# ============================ Example ============================
# >>> getProperties("contacts")
# ['about_us',
# 'address',
# 'address2',
# 'annualrevenue',
# 'city',
# ...
# ]
# ============================ Example ============================
async def getProperties(object_type):
    url = "https://api.hubapi.com/crm/v3/objects/{0}/properties".format(object_type)
    response = await loop.run_in_executor(None, functools.partial(requests.request, "GET", url, headers=headers, params=querystring))
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        raise Exception("Network Error")

# Input: None
# Output: Pipeline information about "deals" object (info about stage ids)
# ============================ Example ============================
# >>> getDealsPipelineInfo()
# {"results":[{"label":"Sales Pipeline","displayOrder":0,"active":true,"stages":[{"label":"PSIM - Lead","displayOrder":0,"metadata":{"isClosed":"false","probability":"0.2"},"stageId":"appointmentscheduled","createdAt":0,"updatedAt":1597026126964,"active":true}, ... "objectType":"DEAL","objectTypeId":"0-3","pipelineId":"default","createdAt":0,"updatedAt":1597026126964,"default":true}]}'
# ============================ Example ============================
def getDealsPipelineInfo():
    url = "https://api.hubapi.com/crm-pipelines/v1/pipelines/deals?hapikey=" + api_key
    response = requests.request("GET", url)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        raise Exception("Network Error")

# dealstage =... PSIM - Lead: appointmentscheduled, PSIM - Quoted: qualifiedtobuy // for both SUPER and TEST ACCOUNT
def updateDealObject(deal_id, url_drive_quote, dealstage):
    url = "https://api.hubapi.com/crm/v3/objects/deals/" + deal_id
    payload = "{\"properties\":{\"url_drive_quote\":\"%s\",\"dealstage\":\"%s\"}}" % (url_drive_quote, dealstage)
    response = requests.request("PATCH", url, data=payload, headers=headers, params=querystring)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        raise Exception("Network Error")