__author__ = 'Benjamin Zwettler'


import ipaddress
import subprocess

"""ein adminscript das eine ip + subnetsuffix einliest ud alle hosts in diesem netz pingt"""

network = ipaddress.ip_network(input("bitte ip addresse mit netzsuffix eingeben"), strict=False)
for ip in network.hosts():
    subprocess.run(["ping",str(ip)], creationflags=subprocess.CREATE_NEW_CONSOLE)
