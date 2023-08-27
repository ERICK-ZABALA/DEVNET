from ncclient import manager
import xml.dom.minidom
import xmltodict
from pprint import pprint
router = {"host":"ios-xe-mgmt-latest.cisco.com", "port":"10000",
          "username":"developer", "password":"C1sc0123" }

netconf_filter = """
<filter>
 <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
  <interface>
   <name>GigabitEthernet2</name>
  </interface>
 </interfaces>
<interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
 <interface>
  <name>GigabitEthernet2</name>
 </interface>
</interfaces-state>
</filter>  
"""

with manager.connect(host=router["host"], port=router["port"], 
                     username=router["username"], password=router["password"], 
                     hostkey_verify=False) as m:
    
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)
        # Get the running config on the filtered out interface
        print('Connected')
        interface_netconf = m.get(netconf_filter)
        print("getting running config:")

        #interface_netconf = m.get(netconf_filter)
        #xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
        #print(xmlDom.toprettyxml(indent=" "))
        #print('*' * 25 + 'Break' + '*' * 50)

        # XML To DICT convert xml to python dictinary 
        interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]
        pprint(interface_python)

        name = interface_python['interfaces']['interface']['name']['#text']
        print(name)

        config = interface_python["interfaces"]["interface"]
        op_state = interface_python["interfaces-state"]["interface"]

        print("Start")
        print(f"Name: {config['name']['#text']}")
        print(f"Description: {config['description']}")
        print(f"Packets In {op_state['statistics']['in-unicast-pkts']}")



        
    
    m.close_session()
