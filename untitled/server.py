import os
import socket
import sys


o = open("file.txt", 'w')
sock = socket.socket()
sock.bind(("", 8080))
sock.listen(10)
req = []
tcpre = {}
try:
    while True:
        client_socket, remote_address = sock.accept()
        address = remote_address[0]
        child_pid = os.fork()
        if child_pid == 0:
            while True:
                request = client_socket.recv(1024)
                client_socket.send(request.upper())
                request_str = request.decode("utf-8")
                print('{} : {}'.format(address, request_str))
                o.write('{} : {}'.format(address, request_str) + '\n')
            client_socket.close()
            sys.exit()
        else:
            client_socket.close()
except KeyboardInterrupt:
    sock.close()
    o.close()