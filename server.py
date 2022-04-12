#!/usr/bin/python3

import socket

servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#hnam = "google.com"
#host = 'tuipaqui'
#host = socket.gethostbyname(hnam)
host = socket.gethostname()
port = 444

servsock.bind((host, port))
servsock.listen(3)

while True:
    clientsocket, address = servsock.accept()
    print("Connection recieved from: %s " % str(address))
    message = 'Thank you for your connection Mr. %s.' % str(address) + "\r\n"
    clientsocket.send(message.encode('ascii'))
    clientsocket.close()
