import os

print("*"*100)
print('\n')
print("\t\t\t\t\tEnter your choice")
print('\n')
print("*"*100)
print('\n')

print("1.ARP Cache Poisoner")
print("2.Prober")
print("3.Simple Port Scan")
print("4.Network Sniffer")
print("5.Sub Domain Finder")
print('6. Advanced Port Scan')
print('7. Ping of Death')
print('8.Smurf Attack')

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
elif choice==6:
    os.system("sudo python3 scans.py")
elif choice==7:
    os.system("sudo python3 pingOfDeath.py")
elif choice==8:
    os.system("sudo python3 smurf.py")
else:
    print("Invalid option selected")