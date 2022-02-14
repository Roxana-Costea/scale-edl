import ipaddress

net4 = ipaddress.ip_network('192.0.2.0/21', False)
for x in net4.hosts():
    print(x)


