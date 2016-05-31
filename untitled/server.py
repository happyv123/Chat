import os
import socket
import sys


sock = socket.socket()
sock.bind(("", 8080))
sock.listen(10)
req=[]
while True:
    client_socket, remote_address = sock.accept()
    child_pid = os.fork()
    if child_pid == 0:
        while True:
            request = client_socket.recv(1024)
            client_socket.send(request.upper())
            request_str = request.decode("utf-8")
            req.append('{} : {}'.format(client_socket.getpeername(), request_str))
            for i in range(0, len(req)):
                print(req[i])
            print('{} : {}'.format(client_socket.getpeername(), request_str))
        sys.exit()
    else:
        pass

sock.close()