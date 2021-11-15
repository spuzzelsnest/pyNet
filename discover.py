#!/usr/bin/python3

import shlex
import subprocess
import sys
import os


def sendIcmpEcho(target, out_xml):
    out_xml = os.path.join(out_xml,'logs/icmp_echo_host_discovery.xml')
    nmap_cmd = f"/usr/bin/nmap {target} -n -sn -PE -vv -oX {out_xml}"                     
    sub_args = shlex.split(nmap_cmd)
    subprocess.Popen(sub_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    makeInvokerOwner(out_xml)
    print('icmp done')


def sendIcmpNetmask(target, out_xml):
    out_xml = os.path.join(out_xml,'logs/icmp_netmask_host_discovery.xml')
    nmap_cmd = f"/usr/bin/nmap {target} -n -sn -PM -vv -oX {out_xml}"
    sub_args = shlex.split(nmap_cmd)
    subprocess.Popen(sub_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    makeInvokerOwner(out_xml)
    print('netmask done')


def sendIcmpTimestamp(target, out_xml):
    out_xml = os.path.join(out_xml,'logs/icmp_timestamp_host_discovery.xml')
    nmap_cmd = f"/usr/bin/nmap {target} -n -sn -PP -vv -oX {out_xml}"
    sub_args = shlex.split(nmap_cmd)
    subprocess.Popen(sub_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    makeInvokerOwner(out_xml)
    print('host discovery done')


def sendTcpSyn(target, out_xml):
    out_xml = os.path.join(out_xml,'logs/tcp_syn_host_discovery.xml')
    nmap_cmd = f"/usr/bin/nmap {target} -PS21,22,23,25,80,113,443 -PA80,113,443 -n -sn -T4 -vv -oX {out_xml}"
    sub_args = shlex.split(nmap_cmd)
    subprocess.Popen(sub_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    makeInvokerOwner(out_xml)
    print('tcp done')


def tcpSynPortScan(target, out_xml,):
    out_xml = os.path.join(out_xml,'top_1000_portscan.xml')
    nmap_cmd = f"/usr/bin/nmap {target} --top-ports 1000 -n -Pn -sS -T4 --min-parallelism 100 --min-rate 64 -vv -oX {out_xml}"
    sub_args = shlex.split(nmap_cmd)
    subprocess.Popen(sub_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    makeInvokerOwner(out_xml)


def makeInvokerOwner(path):
    uid = os.environ.get('SUDO_UID')
    gid = os.environ.get('SUDO_GID')
    if uid is not None:
        os.chown(path, int(uid), int(gid))


def is_root():
    if os.geteuid() == 0:
        return True
    else:
        return False


def main():
    if not is_root():
        print('[!] The discovery probes in this script requires root privileges')
        sys.exit(1)
    
    target = input("what target are you trying to discover? ")

    sendIcmpEcho(target, os.getcwd())
    sendIcmpNetmask(target, os.getcwd())
    sendIcmpTimestamp(target, os.getcwd())
    sendTcpSyn(target, os.getcwd())

    print("=" * 60)


if __name__ == '__main__':
    main()
