import socket

HOST = '127.0.0.1'
PORT = 63222

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello World - my dick is bigger than yours')
    data = s.recv(1025)

print('Recieved', repr(data))



