__author__ = 'Benjamin Zwettler'


import ipaddress
import subprocess

network = ipaddress.ip_network(input("bitte ip addresse mit netzsuffix eingeben"), strict=False)
for ip in network.hosts():
    subprocess.run(["ping",str(ip)], creationflags=subprocess.CREATE_NEW_CONSOLE)
