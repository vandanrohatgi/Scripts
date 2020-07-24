from scapy.all import IP,ICMP,TCP,sr1
import sys

target=input('Enter the IP address of target')
ping=IP(dst=target)/ICMP()
ans=sr1(ping,timeout=5,verbose=False)

if ans==None:
	print('Target is not reachable!')
	sys.exit()


print('Choose a type of scan')
print('1. Syn Scan')
print('2. Xmas Scan')
print('3. Ack Scan')
print('4. Fin Scan')
print('5. Null Scan')

def syn(target):
	pkt=IP(dst=target)/TCP(dport=1,flags='S')
	for port in range(1,1001):
		pkt.dport=port
		ans=sr1(pkt,timeout=1,verbose=False)
		if ans!=None and ans[TCP].flags=='SA':
			print('Port {} open'.format(port))


def xmas(target):
	pkt=IP(dst=target)/TCP(dport=1,flags='FPU')
	for port in range(1,1001):
		pkt.dport=port
		ans=sr1(pkt,timeout=1,verbose=False)
		if ans==None or ICMP in ans:
			print('Port {} may be open / '.format(port))
		elif ans[TCP].flags=='R':
			pass
			#print('port {} is definitely closed '.format(port))
			
def null(target):
	pkt=IP(dst=target)/TCP(dport=1)
	for port in range(1,1001):
		pkt.dport=port
		ans=sr1(pkt,timeout=1,verbose=False)
		if ans==None or ICMP in ans:
			print('Port {} may be open / '.format(port))
		elif ans[TCP].flags=='R':
			pass
			#print('port {} is definitely closed '.format(port))

def fin(target):
	pkt=IP(dst=target)/TCP(dport=1,flags='F')
	for port in range(1,1001):
		pkt.dport=port
		ans=sr1(pkt,timeout=1,verbose=False)
		if ans==None or ICMP in ans:
			print('Port {} may be open / '.format(port))
		elif ans[TCP].flags=='R':
			pass
			#print('port {} is definitely closed '.format(port))

def ack(target):
	pkt=IP(dst=target)/TCP(dport=1,flags='A')
	for port in range(1,1001):
		pkt.dport=port
		ans=sr1(pkt,timeout=1,verbose=False)
		if ans!=None and ans[TCP].flags=='R':
			print('port {} is unfiltered'.format(port))

while True:
	choice=int(input('Your choice:'))
	if choice in range(0,6):
		break
	else:
		print('Incorrect Option!')

if choice==1:
	syn(target)
elif choice==2:
	#xmas(target)
	pass
elif choice==3:
	#ack(target)
	pass
elif choice==4:
	#fin(target)
	pass
elif choice==5:
	#null(target)
	pass





