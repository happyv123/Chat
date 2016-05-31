import os
import socket
import sys


sock = socket.socket()
sock.bind(("", 8080))
sock.listen(10)

while True:
    client_socket, remote_address = sock.accept()
    child_pid = os.fork()
    if child_pid == 0:
        request = client_socket.recv(1024)
        client_socket.send(request.upper())
        print ('(child {}) {} : {}'.format(client_socket.getpeername(), request))
        client_socket.close()
        sys.exit()
    else:
        client_socket.close()

sock.close()