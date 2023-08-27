import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url_base = 'https://sandbox-nso-1.cisco.com:443/restconf/data/tailf-ncs:devices/device'
auth = ("developer", "Services4Ever")
headers = {'Accept':'application/yang-data+json'}

# https://sandbox-nso-1.cisco.com:443/api/running/devices/device

response = requests.get(url= f'{url_base}', auth=auth, headers=headers, verify=False)

response_text = response.text

#print (type(response_text))
#print (response_text)
# repair json output https://jsonformatter.org/json-parser



with open('response.json', 'w') as file:
    file.write(response_text)

with open('response_fix.json', 'r') as file_fix:
    data = json.load(file_fix)

devices = data['tailf-ncs:device']
    

for device in devices:
    print(f"Name: {device['name']}")
    print(f"IP: {device['address']}")
    print(f"SSH Port: {device['ssh']}")
    print(f"Auth Group: {device['authgroup']}")
    print(" ")
        