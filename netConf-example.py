import getpass, requests, enquiries, ipaddress
from netifaces import interfaces, ifaddresses, AF_INET
from jnpr.junos import Device


#user = input("username: ")
#psswd = getpass.getpass(prompt='Password: ', stream=None)

ifList = []
devices = []
options = []

extIP = requests.get('http://ifconfig.io/ip').text
print(f'\nexternal IP: ' + extIP)

print("\nFound the following interface(s)\n")

for ifaceName in interfaces():
    addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
    ifList.append(ifaceName)
    print(ifaceName, ', '.join(addresses))


i = len(ifList)

print(f'\nfound {i} interfaces')

for idx, val in enumerate(ifList):
    options.append(ifList[idx])
    #print(f'{idx +1}:  {val}')

choice = enquiries.choose('Select an interface', options)

print(choice)    

print(f'{ifaddresses(choice)}')


#for switch in devices:

#   connection = Device(host=switch, user=user, password=psswd)

#    connection.open()
#    showVer =  connection.rpc.get_software_information({'format': 'json'})
#    connection.close()

#    print(showVer)

