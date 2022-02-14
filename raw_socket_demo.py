import socket # for basic socket functions
import sys # for system level commands
import struct # for establishing the packet structure

# create framework
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
except socket.error as msg:
    print(msg)
    sys.exit()

    packet = ''

src_ip = '10.1.0.2'
dst_ip = '10.3.0.2'

# let's make the rest of the IPv4 Headers
ip_ver_ihl = 69  # This is putting the deimal conversion of 0x45 for version and internet header
ip_tos = 0  # This combines the DSCP and ECN fields
ip_len = 0  # The kernel will fill this in for us automatically
ip_id =12345  # This sets the ip identification for the packet
ip_frag = 0  # This set the fragmentation to off
ip_ttl = 64 # This determines the TTL of the packet when leaving
ip_proto = 16  # This set the IP protocol to CHAOS (note UDP = 17 and TCP = 6)
ip_check = 0  # The kernel will fill this in for us
ip_src_addr = socket.inet_aton(src_ip) # inet_aton takes string input and will convert to 32 bit binary number
ip_dst_addr = socket.inet_aton(dst_ip)

ip_header = struct.pack('!BBHHHBBH4s4s', ip_ver_ihl, ip_tos, ip_len, ip_id, ip_frag, ip_ttl, ip_proto, ip_check, ip_src_addr, ip_dst_addr)  # ! means put this in network order (big Endian), B means one byte, H means half word (2 bytes), 4smeans word (4 bytes)

message = b'This is your message'
packet = ip_header + message # This combines the IP header with our message

s.sendto(packet, (dst_ip,0))

s.close()