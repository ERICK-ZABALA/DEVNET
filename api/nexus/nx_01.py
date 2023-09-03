# CONFIGURE NX API
# configure terminal
# feature nxapi
#  nxapi sandbox
# exit
# wr

import requests
import json

url = "https://sbx-nxos-mgmt.cisco.com/ins"

payload = json.dumps({
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show ip int br",
    "output_format": "json"
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YWRtaW46QWRtaW5fMTIzNCE=',
  'Cookie': 'nxapi_auth=dzqnf:LbQuhnRkQZ4ybOwtbzISYfCXUl4='
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)
