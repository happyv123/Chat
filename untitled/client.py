import socket

while True:
    sock = socket.socket()
    inp = input("Enter msg: ")
    sock.connect(("192.168.0.9", 8080))
    if inp == '':
        inp =' '
    sock.send(inp.encode("utf-8"))
    request = sock.recv(1024)
    print(request.decode("utf-8"))
    sock.close()