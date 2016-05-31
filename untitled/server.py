import os
import socket
import sys


o = open("file.txt", 'w')
sock = socket.socket()
sock.bind(("", 8080))
sock.listen(10)
req = []
try:
    while True:
        client_socket, remote_address = sock.accept()
        child_pid = os.fork()
        if child_pid == 0:
            request = client_socket.recv(1024)
            client_socket.send(request.upper())
            request_str = request.decode("utf-8")
            print('{} : {}'.format(client_socket.getpeername(), request_str))
            o.write('{} : {}'.format(client_socket.getpeername(), request_str) + '\n')
            client_socket.close()
            sys.exit()
        else:
            client_socket.close()
except KeyboardInterrupt:
    sock.close()
    o.close()