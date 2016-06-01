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
        login = client_socket.recv(1024).decode('utf-8')
        address = remote_address[0]
        tcpre = {address: login}
        child_pid = os.fork()
        if child_pid == 0:
            while True:
                o = open("file.txt", 'a')
                request = client_socket.recv(1024)
                if request.decode('utf-8') == "__disc__":
                    print('User {} has left'.format(tcpre[address]))
                    client_socket.close()
                    sys.exit()
                client_socket.send(request.upper())
                request_str = request.decode("utf-8")
                print('{} : {}'.format(tcpre[address], request_str))
                o.write('{} : {}'.format(tcpre[address], request_str) + '\n')
                o.close()
        else:
            client_socket.close()
except KeyboardInterrupt:
    sock.close()
    o.close()
except ConnectionResetError:
    print('User {} has left'.format(tcpre[address]))
    client_socket.close()
    sys.exit()