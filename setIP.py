import socket, struct, fcntl

ifList = []
SIOCSIFADDR = 0x8916
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def setIpAddr(iface, ip):
    bin_ip = socket.inet_aton(ip)
    ifreq = struct.pack('16sH2s4s8s', iface, socket.AF_INET, '\x00' * 2, bin_ip, '\x00' * 8)
    fcntl.ioctl(sock, SIOCSIFADDR, ifreq)


setIpAddr('eno1', '192.168.10.21')



for ifaceName in interfaces():
    addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
    ifaceName.append(ifList)

    #print(ifaceName, ', '.join(addresses))