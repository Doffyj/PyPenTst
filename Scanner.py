#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome, day1")
print("<------------->")

ip_addr = input("Mete la ip a escanear: ")
print("IP: ", ip_addr)
type(ip_addr)

resp = input(""" \nQue tipo de scan quieres pisha:
 /  1) SYN/ACK Scan
|   2) UDP Scan
 \  3) Scanolargo
Input: """)
print("Elegiste la opcion: ", resp)

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-2048', '-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Puertos abiertos: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Puertos abiertos: ", scanner[ip_addr]['udp'].keys())
elif resp == 3:
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-2048', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Puertos abiertos: ", scanner[ip_addr]['udp'].keys())
else:
    print("Bella ciao")