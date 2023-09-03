#!/workspaces/DEVNET/api/nx-api/nexus/bin/python

import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

controler = 'sandboxapicdc.cisco.com'

def getTicket(controler):
    url = "https://" + controler + "/api/aaaLogin.json"
    payload = {
        "aaaUser":{
            "attributes":{
                "name":"admin",
                "pwd":"!v3G@!4@Y"
                }
            }
        }
    
    headers = {
        'Content-Type': 'application/json',
        'Accept':'application/json'
        }
    
    
    response = requests.post(url=url, data=json.dumps(payload), headers=headers, params={"format": "json"}, verify=False)
    
    if response.status_code == 200:
        response_data = response.json()
        ticket = response_data.get("response", {}).get("serviceTicket")
        if ticket:
            print("Ticket:", ticket)
        else:
            print("No se pudo obtener el ticket de servicio.")
    else:
        print("Error en la solicitud:", response.status_code, response.text)


getTicket(controler)