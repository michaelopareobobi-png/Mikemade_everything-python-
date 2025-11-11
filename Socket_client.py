import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('localhost',8080))

print(client.recv(1024).decode())