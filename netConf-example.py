import getpass, requests, enquiries, socket, struct, fcntl, ipaddress
from netifaces import interfaces, ifaddresses, AF_INET


#user = input("username: ")
#psswd = getpass.getpass(prompt='Password: ', stream=None)

ifList = []
devices = []
options = []

host_name = socket.gethostname()


extIP = requests.get('http://ifconfig.io/ip').text
print(f'\n{host_name} is on external IP: ' + extIP)

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



