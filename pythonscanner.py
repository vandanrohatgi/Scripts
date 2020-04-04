'''
usage : python3 pythonscanner.py <target>
'''

import socket
import sys
import time

#start timer 
t1=time.time()

#handle exceptions
try:
    nameofhost=sys.argv[1]
except IndexError:
    print("usage: python pythonscanner.py <name of host>")
    sys.exit()

#print a pretty banner
print('*'*50)
print("              PORT        SCANNER              ")
print('*'*50)
print("checking for : {} \n".format(nameofhost))


ip=socket.gethostbyname(nameofhost)

print("ip address={} \n".format(ip))

#start scanning ports
for x in range(1,65535):
    try :
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip,x))
        try:
            service=socket.getservbyport(x,'tcp')
        except:
            service="service not found"
        print("PORT {}: {}".format(x,service))       
        s.close()
    except socket.error:
        pass

#end timer
t2=time.time()
print("took {} seconds".format(t2-t1))
