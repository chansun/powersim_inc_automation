from googleAPI import *

# Input: Header data
# Output: Title for the copy quote
# ============================ Example ============================
# >>> makeCopyTitle(header_data)
# 'Quote 906636709 - Lite-On Singapore Pte. Ltd. (v.11)'
# ============================ Example ============================
def makeCopyTitle(header_data):
    return "Quote {0} - {1} (v.{2})".format(header_data["quote_number"], header_data["company_name"], header_data["quote_version"])

# Input: Header data
# Output: Request data
def makeRequests(header_data):
    requests = []
    requests.append(
        {
            "replaceAllText": 
            {
                "replaceText": header_data["quote_version"],
                "containsText": 
                {
                    "text": "[q_v]",
                    "matchCase": "true"
                }
            }
        }
    )
    requests.append(
        {
            "replaceAllText":
            {
                "replaceText": header_data["preparer_name"],
                "containsText": 
                {
                    "text": "[Preparer Name]",
                    "matchCase": "true"
                }
            }
        }
    )
    requests.append(
        {
            "replaceAllText": 
            {
                "replaceText": header_data["quote_number"],
                "containsText": 
                {
                    "text": "[Quotation Number]",
                    "matchCase": "true"
                }
            }
        }
    )
    requests.append(
        {
            "replaceAllText": 
            {
                "replaceText": header_data["mon"],
                "containsText": 
                {
                    "text": "[Mon]",
                    "matchCase": "true"
                }
            }
        }
    )
    requests.append(
        {
            "replaceAllText": 
            {
                "replaceText": header_data["day"],
                "containsText": 
                {
                    "text": "[Day]",
                    "matchCase": "true"
                }
            }
        }
    )
    requests.append(
        {
            "replaceAllText": 
            {
                "replaceText": header_data["year"],
                "containsText": 
                {
                    "text": "[Year]",
                    "matchCase": "true"
                }
            }
        }
    )
    requests.append(
        {
            "replaceAllText": 
            {
                "replaceText": header_data["prepared_for"],
                "containsText": 
                {
                    "text": "[Person Name]",
                    "matchCase": "true"
                }
            }
        }
    )
    requests.append(
        {
            "replaceAllText": 
            {
                "replaceText": header_data["company_name"],
                "containsText": 
                {
                    "text": "[Company Name]",
                    "matchCase": "true"
                }
            }
        }
    )
    requests.append(
        {
            "replaceAllText": 
            {
                "replaceText": header_data["country_or_region"],
                "containsText": 
                {
                    "text": "[COUNTRY or REGION]",
                    "matchCase": "true"
                }
            }
        }
    )
    return requests