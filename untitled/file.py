import socket


server_socket = socket.socket()
server_socket.bind(('', 8080))
server_socket.listen(100000)
Req = []

while True:
    client_socket, address = server_socket.accept()
    try:
        request = client_socket.recv(1024)
        request_str = request.decode("utf-8")
        Req.append('{} : {}'.format(client_socket.getpeername(), request_str))
        print (Req)
        print('{} : {}'.format(client_socket.getpeername(), request_str))
        client_socket.send(address[0].encode("utf-8") + b' : ' + request_str.encode("utf-8"))
        client_socket.close()

    except:
        pass

server_socket.close()