from jnpr.junos import Device

connection = Device(host='ip', user='user', password='pass')

connection.open()
showVer =  connection.rpc.get_software_information({'format': 'json'})
connection.close()

print(showVer)

