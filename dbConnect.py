#!/usr/bin/python3

import sqlite3
import xml.etree.ElementTree as ET


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    return conn


def create_db(conn):
    createHostDiscoveryTable="""CREATE TABLE IF NOT EXISTS HostDiscovery (
            id integer PRIMARY KEY,
            IP text NOT NULL,
            Status text NOT NULL,
            ICMP_Echo text NOT NULL);"""
    try:
        c = conn.cursor()
        c.execute(createHostDiscoveryTable)
    except Exception as e:
        print(e)


def insert_content(conn, content):
    sql = ''' INSERT INTO HostDiscovery(IP,Status,ICMP_Echo)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, content)
    return cur.lastrowid


def main():
    db_file = 'nmap.db'
    conn = create_connection(db_file)
    create_db(conn)

 # Parse XML
    in_xml_echo = 'logs/icmp_echo_host_discovery.xml'

    # Load ICMP Echo XML
    xml_tree_echo = ET.parse(in_xml_echo)
    xml_root_echo = xml_tree_echo.getroot()

    # Load ICMP Echo XML
    for host in xml_root_echo.findall('host'):
        echo_ip = host.find('address').get('addr')
        echo_state = host.find('status').get('state')
        echo_reason = host.find('status').get('reason')
        
        # Insert results into database
        insert_content(conn, (echo_ip, echo_state, echo_reason))
        conn.commit()


if __name__ == '__main__':
    main()
