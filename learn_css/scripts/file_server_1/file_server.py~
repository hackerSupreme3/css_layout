import socket

HOST = "127.0.0.1"
PORT = 60100

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    clnt, addr = s.accept()
    with clnt:
        page = open('test.html', 'rb')
        clnt.sendfile(page, offset=0)

