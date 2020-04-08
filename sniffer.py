import socket
import struct
import sys


table={0: 'HOPOPTS', 1: 'ICMP', 2: 'IGMP', 41: 'IPV6', 4: 'IPIP', 6: 'TCP', 8: 'EGP', 12: 'PUP', 17: 'UDP', 22: 'IDP', 29: 'TP', 43: 'ROUTING', 44: 'FRAGMENT', 46: 'RSVP', 47: 'GRE', 50: 'ESP', 51: 'AH', 58: 'ICMPV6', 59: 'NONE', 60: 'DSTOPTS', 103: 'PIM', 132: 'SCTP', 255: 'RAW'}


def extract(packet):
    ethernet = packet[0:14]
    ip=packet[14:34]
    tcp=packet[34:54]
    data=packet[54:]    
    eth_header=struct.unpack("!6s6s2s", ethernet)
    tcp_hdr=struct.unpack("!HHII2sH2sH", tcp)
    ip_header=struct.unpack("!1s1s1H1H2s1B1B2s4s4s", ip)
    print(socket.inet_ntoa(ip_header[9])+':'+str(tcp_hdr[0]),end='    |      ')
    print(socket.inet_ntoa(ip_header[8])+':'+str(tcp_hdr[1]),end='     |       ')
    print(table.get(ip_header[6],'Protocol not available')+'      |      '+str(ip_header[5]),end='    |    ')
    print(bytes((x for x in data if x >= 0x20 and x < 127)))
    print('\n')




print('WELCOME TO PACKET SNIFFER')
print('PRESS CTRL+C TO STOP')
print('DESTINATION IP:PORT      | SOURCE IP:PORT      | PROTOCOL      | TTL      | DATA ')
sock=socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0800))
try:
    while True:
        pkt=sock.recv(2048)
        extract(pkt)
except:
    sys.exit()

