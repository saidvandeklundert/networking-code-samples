# show interfaces terse and show interfacex xe-2/0/2 example

from jnpr.junos import Device
from lxml import etree

username='lab'
password='lab123'

# show interface ters

dev = Device(host='10.0.0.242', user=username, password=password, normalize=True)

dev.open()

data1 = dev.rpc.get_interface_information(terse=True)
print(etree.tostring(data1, encoding='unicode'))

# show interface ters for interface xe-2/0/2
data2 = dev.rpc.get_interface_information(interface_name='xe-2/0/2')
print(etree.tostring(data2, encoding='unicode'))

dev.close()

