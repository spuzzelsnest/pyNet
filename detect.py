#!/usr/bin/python3

import xml.etree.ElementTree as ET
import sqlite3
import subprocess
import shlex
import os
import sys


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    return conn


def select_content(conn):
    sql = """SELECT IP 
              FROM HostDiscovery 
              WHERE Status = 'up'
              AND ICMP_Echo != 'localhost-response'
              """
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    return rows


def tcpSynPortScan(target, out_xml,):
    out_xml = os.path.join(out_xml,'logs/top_1000_portscan.xml')
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
        print('[!] TCP/SYN scans requires root privileges')
        sys.exit(1)

    db_file = 'nmap.db'
    conn = create_connection(db_file)
    live_hosts = select_content(conn)
    for host in live_hosts:
        target = host[0]
        print(f'Scanning {target} against top 1000 ports')
        tcpSynPortScan(target, os.getcwd())


if __name__ == '__main__':
    main()
