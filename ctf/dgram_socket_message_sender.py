import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ipaddr = '10.10.0.40'
port = 10000

s.sendto(b'Disturbed', (ipaddr, port))

response, conn = s.recvfrom(1024)

print(response.decode())

s.close()
