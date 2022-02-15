import ipaddress
import time




ip = str(ipaddress.IPv4Address('192.169.0.0'))
ip2 = str(ipaddress.IPv4Address('192.169.0.0')+256)
print(ip2)
ip3 = str(ipaddress.IPv4Address('192.169.1.0')+256)
print(ip3)
ip4 = str(ipaddress.IPv4Address('192.169.2.0')+256)
print(ip4)
split_ip = ip.split('.')
split_ip2 = ip2.split('.')
split_ip3 = ip3.split('.')
split_ip4 = ip4.split('.')
#print(type(split_ip))



file = open('ip-list-scale-v2.txt', 'a')



for x in range (1, 256):
#print(split_ip[0] + '.' +split_ip[1] +'.' + split_ip[2]+'.'+ str(x) + '/24 ')
    file.write(split_ip[0] + '.' +split_ip[1] + '.' + split_ip[2]+'.' + str(x) + '/21 \n')
for x in range(1, 256):
    file.write(split_ip2[0] + '.' + split_ip2[1] + '.' + split_ip2[2] + '.' + str(x) + '/21 \n')
for x in range(1, 256):
    file.write(split_ip3[0] + '.' + split_ip3[1] + '.' + split_ip3[2] + '.' + str(x) + '/21 \n')
for x in range(1, 256):
    file.write(split_ip4[0] + '.' + split_ip4[1] + '.' + split_ip4[2] + '.' + str(x) + '/21 \n')



file.close()
