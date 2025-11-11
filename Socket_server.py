import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('socket created')

server.bind(('localhost',8080))

server.listen(3)

while True:
    client,addr=server.accept()
    print('connected from',addr)
    client.send(bytes('Welcome hero ;)','utf-8'))
    client.close()