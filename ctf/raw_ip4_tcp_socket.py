import socket # for basic socket functions
import sys # for system level commands
import struct # for establishing the packet structure
import array # This is for the TCP checksum

# create framework
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
except socket.error as msg:
    print(msg)
    sys.exit()

    packet = ''

src_ip = '10.10.0.40'
dst_ip = '172.16.40.10'

# let's make the rest of the IPv4 Headers
ip_ver_ihl = 69  # This is putting the deimal conversion of 0x45 for version and internet header
ip_tos = 0  # This combines the DSCP and ECN fields
ip_len = 0  # The kernel will fill this in for us automatically
ip_id = 2020  # This sets the ip identification for the packet
ip_frag = 0  # This set the fragmentation to off
ip_ttl = 64 # This determines the TTL of the packet when leaving
ip_proto = 6  # This set the IP protocol to CHAOS (note UDP = 17 and TCP = 6)
ip_check = 0  # The kernel will fill this in for us
ip_src_addr = socket.inet_aton(src_ip) # inet_aton takes string input and will convert to 32 bit binary number
ip_dst_addr = socket.inet_aton(dst_ip)

ip_header = struct.pack('!BBHHHBBH4s4s', ip_ver_ihl, ip_tos, ip_len, ip_id, ip_frag, ip_ttl, ip_proto, ip_check, ip_src_addr, ip_dst_addr)  # ! means put this in network order (big Endian), B means one byte, H means half word (2 bytes), 4smeans word (4 bytes)

# make tcp header
tcp_src = 54321  # source port
tcp_dst = 12345  # destination port
tcp_seq = 90210  # seuence number
tcp_seq_ack = 30905  #tcp ack seq num
tcp_data_off = 5  # Data offset specifying the size of the TCP header (x4 so offset will actually be 20)
tcp_reserve = 0  # the 3 reserve bits and ns flag in reserve field, generally not used but must be included in packet
tcp_flags = 0  # TCP flags (0 means all off)
tcp_win = 5620  # maximum allowed window reordered to network order
tcp_chk = 0  #tcp checksum will be calculated later
tcp_urg_ptr = 0  #urgent pointer (only used if urg flag is set)

# combine the shifted (left) 4 bit tcp offset and the reserve field
tcp_off_res = (tcp_data_off << 4) + tcp_reserve # if we start at binary 1 we are shifting 4 bits to the left (ie 0000111 wil become 1111000)
# TCP flag fileds (bits starting from right to left)
tcp_fin = 0  # finished
tcp_syn = 1  # synchronization request
tcp_rst = 0  # rest
tcp_psh = 0  # push
tcp_ack = 0  # acknowledgement
tcp_urg = 0  #urgent
tcp_ece = 0  # explicit congestion
tcp_cwr = 0  # congestion window reduced

# combine the TCP flags by left shifting the bit! and add them
tcp_flags = tcp_fin + (tcp_syn << 1) + (tcp_rst <<2) + (tcp_psh << 3) + (tcp_ack <<4) + (tcp_urg <<5) + (tcp_ece << 6) + (tcp_cwr <<7)  # bitshift 1 to left and put tcp syn there, etc.

# ! in pack sepcifies big endian or network order
tcp_hdr = struct.pack('!HHLLBBHHH', tcp_src, tcp_dst, tcp_seq, tcp_seq_ack, tcp_off_res, tcp_flags, tcp_win, tcp_chk, tcp_urg_ptr) # L means 32 bit word as an integer

user_data = b'HERE IS MY MESSAGE'

#pseudoheader fields
src_addr = socket.inet_aton(src_ip)
dst_addr = socket.inet_aton(dst_ip)
reserved = 0
protocol = socket.IPPROTO_TCP
tcp_len = len(tcp_hdr) + len(user_data)

# pack pseudoheader
ps_hdr = struct.pack('!4s4sBBH', src_addr, dst_addr, reserved, protocol, tcp_len)
ps_hdr = ps_hdr + tcp_hdr + user_data

# take pesudo header, split into bits and calculate checksum
def checksum(data):
    if len(data) % 2 !=0:
        data == b'\0' # pad with a 0 if we have an odd amount going out in the data
    res = sum(array.array("H", data))
    res = (res >> 16) + (res & 0xffff)
    res = res >> 16
    return (~res) & 0xffff

tcp_chk = checksum(ps_hdr)
tcp_hdr = struct.pack('!HHLLBBH', tcp_src, tcp_dst, tcp_seq, tcp_seq_ack, tcp_off_res, tcp_flags, tcp_win) + struct.pack('H', tcp_chk) + struct.pack ('!H', tcp_urg_ptr)

# Combine all of the headers and the user data
packet = ip_header + tcp_hdr + user_data

#  Send the packet!! Woot!
s.sendto(packet, (dst_ip,0))
