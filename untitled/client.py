import socket


sock = socket.socket()
sock.connect(("192.168.0.9", 8080))
while True:
    inp = input("Enter msg: ")
    if inp == '':
        inp =' '
    sock.send(inp.encode("utf-8"))
    request = sock.recv(1024)
    print(request.decode("utf-8"))
