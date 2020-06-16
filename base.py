import os

print("*"*100)
print('\n')
print("\t\t\t\t\tEnter your choice")
print('\n')
print("*"*100)
print('\n')

print("1.ARP Cache Poisoner")
print("2.Prober")
print("3.Port-Scanner")
print("4.Network Sniffer")
print("5.Sub Domain Finder")

choice=int(input())
if (choice==1):
    os.system("python3 arp-poison.py")
elif (choice==2):
    os.system("./prober.sh")
elif (choice==3):
    ip=input("Enter the IP Address to scan")
    os.system("python3 pythonscanner.py {}".format(ip))
elif (choice==4):
    os.system("python3 sniffer.py")
elif (choice==5):
    target=input("Enter the target URL")
    os.system("python3 subfinder.py {}".format(target))
else:
    print("Invalid option selected")