#!/usr/bin/python3

import socket

clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = 'tuipaqui'
host = socket.gethostname()
port = 444

clientsock.connect((host, port))

message = clientsock.recv(1024) #cap del mensage recivido

clientsock.close()

print(message.decode('ascii'))
