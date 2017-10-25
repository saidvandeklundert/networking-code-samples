from jnpr.junos import Device
from lxml import etree
import jxmlease

username='lab'
password='lab123'
dev = Device(host='10.0.0.135', user=username, password=password, normalize=True)
dev.open()

rpc = dev.rpc.get_ospf_neighbor_information()
rpc_xml = etree.tostring(rpc, pretty_print=True, encoding='unicode')
dev.close()

# print the XML
print(rpc_xml)

# parse the XML string and place the resulting jxmlease object in the result variable
xmlparser = jxmlease.Parser()
result = jxmlease.parse(rpc_xml)

# print the type, will output <class 'jxmlease.dictnode.XMLDictNode'>
print(type(result))

# print the result, which is the parsed XML
print(result)

# iterate the output at the 'ospf-neighbor' level
for neighbor in result['ospf-neighbor-information']['ospf-neighbor']:
    print(neighbor)                         # print the XML neighbor hierarchy
    print(neighbor['interface-name'])       # print the value of the interface-name
    print(neighbor['neighbor-id'])          # print the value of the neighbor-id

print('after loop')
print(result['ospf-neighbor-information']['ospf-neighbor'])

# display the number of OSPF neighbors:

ospf_neighbors_amount = str(len(result['ospf-neighbor-information']['ospf-neighbor']))

print('\n\n\nThe amount of OSPF neighbors of this node is: ' + ospf_neighbors_amount)

# display all the OSPF neighbors:

# iterate the output at the 'ospf-neighbor' level
for neighbor in result['ospf-neighbor-information']['ospf-neighbor']:
    ospf_neighbor_id = neighbor['neighbor-id']
    ospf_neighbor_interface = neighbor['interface-name']
    print('The node has learned about neighbor {} on interface {}'. format(ospf_neighbor_id, ospf_neighbor_interface))

