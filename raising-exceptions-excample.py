import ipaddress

# some examples on how to raise exceptions

def valid_ip(address):
    try:
        ipaddress.ip_address(address)
        return True
    except:
        return False

def valid_vlan(vlan):
    if int(vlan) <= 1 or int(vlan) >= 4096:
        return False
    else:
        return True

def valid_netmask(netmask):
    if netmask not in range(1, 32):
        return False
    else:
        return True


def createInterface(vlan, ip_network, description, policer):
    ip_address = ip_network.split('/')[0]
    netmask = int(ip_network.split('/')[1])
    interface="""
    set interfaces xe-2/0/2 unit {vlan} description {description}
    set interfaces xe-2/0/2 unit {vlan} vlan-id {vlan}
    set interfaces xe-2/0/2 unit {vlan} family inet mtu 1500
    set interfaces xe-2/0/2 unit {vlan} family inet policer input {policer}
    set interfaces xe-2/0/2 unit {vlan} family inet policer output {policer}
    set interfaces xe-2/0/2 unit {vlan} family inet address {ip_network}
    """.format(vlan=vlan, description=description, ip_network=ip_network, policer=policer)

    if valid_vlan(vlan) is False:
        raise Exception('the supplied VLAN {} does not match the requirements for customer {}'
                        .format(vlan, description))

    if valid_ip(ip_address) == False:
        raise Exception('The supplied IP addres {}'.format(ip_address))

    if valid_netmask(netmask) == False:
        raise Exception('Netmask is not within the range 1-31')

    if '\\' in description or ' ' in description:
        raise Exception('Whitespace and the "\\" character cannot be used in the desciption field')

    return interface

# all is well
print(createInterface('100', '192.168.1.122/31', 'customer-1', '100m'))

# IP address error
#print(createInterface('100', '192.168.1.1222/29', 'customer-2', '100m'))

# subnet mask error
#print(createInterface('100', '192.168.1.122/32', 'customer-3', '100m'))

#VLAN error
#print(createInterface('10001', '192.168.1.1/29', 'customer-4', '100m'))

# description error
#print(createInterface('1000', '192.168.1.1/31', 'customer- 5', '100m'))



