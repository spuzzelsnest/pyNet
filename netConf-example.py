import getpass
import requests
from netifaces import interfaces, ifaddresses, AF_INET
from jnpr.junos import Device


user = input("username: ")
psswd = getpass.getpass(prompt='Password: ', stream=None)

devices = []

extIP = requests.get('http://ifconfig.io/ip').text

print(f'\nexternal IP: ' + extIP)

print("\nFound the following interface(s)\n")

for ifaceName in interfaces():
    addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
    print(ifaceName, ', '.join(addresses))


for switch in devices:

    connection = Device(host=switch, user=user, password=psswd)

    connection.open()
    showVer =  connection.rpc.get_software_information({'format': 'json'})
    connection.close()

    print(showVer)

