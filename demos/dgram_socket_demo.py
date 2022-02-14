import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ipaddr = '127.0.0.1'
port = 54321

s.sendto(b'Hello Again\n', (ipaddr, port))

response, conn = s.recvfrom(1024)
print(response.decode())

s.close()
