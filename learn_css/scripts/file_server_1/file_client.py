import socket

HOST = "127.0.0.1"
PORT = 60100

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    page = s.recv(1024)

print(page)

