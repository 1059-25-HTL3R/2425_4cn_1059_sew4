__author__ = 'Benjamin Zwettler'

import paramiko

time = input("Zeit in min: ")
host = "192.168.241.202"
username = "junioradmin"
keyfile = r"C:\Users\zwett\.ssh\id_ed25519"
pkey = paramiko.Ed25519Key.from_private_key_file(keyfile)
client = paramiko.SSHClient()
policy = paramiko.AutoAddPolicy()
client.set_missing_host_key_policy(policy)
client.connect(host, username=username, pkey=pkey)

stdin, stdout, stderr = client.exec_command('journalctl --since ' + '"' + time + ' minutes ago"')
print(stdout.read().decode())
client.close()
