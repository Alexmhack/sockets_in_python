import socket

HOST = '127.0.0.1'
PORT = 65000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	s.sendall(b'Hello World')
	data = s.recv(1024)

print(f"RECIEVED: {repr(data)}")