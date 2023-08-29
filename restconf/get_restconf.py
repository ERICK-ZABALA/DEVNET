# Request Get
import requests
import json
from pprint import pprint

# Set connection parameters 
router = {
    "ip":"sandbox-iosxe-recomm-1.cisco.com",
    "port":"443",
    "user":"developer",
    "password":"lastorangerestoreball8876"
}

# Set headers

headers = {
    "Accept":"application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

url = f"https://{router['ip']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"
print(url)

response = requests.get(url=url, headers=headers, auth=(router['user'],router['password']), verify=False)

api_data = response.json()

print(api_data)
print()

pprint(api_data["Cisco-IOS-XE-interfaces-oper:interface"]["description"])
pprint("*" * 30)
if api_data["Cisco-IOS-XE-interfaces-oper:interface"]["admin-status"] == "if-state-up":
    print("Interface is Up")


