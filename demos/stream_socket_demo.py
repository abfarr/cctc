import socket

# note this can be done using s= socket() because these are defaults
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ipaddr = '127.0.0.1'
port = 54321

s.connect((ipaddr,port))

s.send(b'Hello!\n')

response, conn = s.recvfrom(1024) # it is recommended that the buffersize is a power of 2

# in order to receive a message that is sent as a bytes-like object you must decode it to utf-8
print(response.decode())

s.close()
