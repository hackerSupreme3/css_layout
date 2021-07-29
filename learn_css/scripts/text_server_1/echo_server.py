import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 63222        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # creates new TCP socket
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1025)
            if not data:
                break
            #conn.sendall(data)
            print(data)

            conn.sendall('Nah bro... I\'m 9\" width, 4\" girth'.encode())
        print('Host:', HOST)

"""

Process for developing a server:
    1. socket()
    2. bind()
    3. listen()
    4. accept()

* Multiple accepts for multiple clients
* socket will sendall()/recv() on socket generated with accept()

Process for developing a client():
    1. socket()
    2. connect()
"""
