'''Usage python3 subfinder.py <target> <output file name(optional)>
'''

import requests
import sys
import time
import re
import multiprocessing
import sys

output=''
#start timer
t1=time.time()
if len(sys.argv)>2:
    output=sys.argv[2]
#get target
try:
    target=str(sys.argv[1])
except:
    print("usage: python3 sublister.py <target>")
    sys.exit()
final_links=[]

#function to find sub-domains on crt.sh
def cert_sh(queue):
    print('[+] Requesting crt.sh')
    certsh="https://crt.sh/?q="
    try:
        links=requests.get(certsh+target)
    except:
        print("couldn't reach crt.sh ")
        sys.exit()

    regex="<TD>(.*?)."+target+"</TD>"
    links1=re.findall(regex,links.text)
    links2=[x+"."+target for x in links1]
    print('crt.sh found {}'.format(len(links2)))
    for y in links2:
        queue.put(y)
    
#find sub-domains on dnsdumpster.com
def dnsdump(queue):
    print('[+] Requesting Dnsdump')
    dns="https://dnsdumpster.com/"
    sess=requests.Session()
    try:
        page=sess.get(dns)
    except:
        print("couldn't reach dnsdumpster.com")
        sys.exit()
    #get csrf token
    html='<input type="hidden" name="csrfmiddlewaretoken" value="(.*?)">'
    token=re.findall(html,page.text)[0]
    payload={'csrfmiddlewaretoken':token,'targetip':target}
    header={'Referer':dns} #to bypass security checks
    links=sess.post(dns,data=payload,headers=header)
    linkreg='<tr><td class="col-md-4">(.*?).'+target+'<br>'
    links1=re.findall(linkreg,links.text)
    links2=[x+'.'+target for x in links1]
    print('dnsdumpster found {}'.format(len(links2)))
    for x in links2:
        queue.put(x)

#start main function
if  __name__ == "__main__":
    queue=multiprocessing.Queue()
    #poor attempt at multi-processing starts here
    P1=multiprocessing.Process(target=dnsdump,args=(queue,))
    P2=multiprocessing.Process(target=cert_sh,args=(queue,))
    P1.start()
    P2.start()
    P1.join()
    P2.join()
    while not(queue.empty()):
        final_links.append(queue.get())
    final_links=set(final_links)
    print('total sub-domains found: {}'.format(len(final_links)))

    #write links to text file if specified in arguements
    if output=='':
        for c in final_links:
            print(c)
    else:
        f=open(output,'w')
        for c in final_links:
            f.write(c+'\n')
        f.close()
    #end timer
    t2=time.time()
    print('completed in {} seconds'.format(t2-t1))