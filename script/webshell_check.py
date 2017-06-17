#-*- coding:utf-8 -*-

import os,sys
from lib.core.Downloader import Downloader,outputer

filename = os.path.join(sys.path[0],"data","web_shell.dic")
payload = []
f = open(filename,'r')
a = 0
for i in f:
    payload.append(i.strip())
    a += 1
    if a==999 :
        break

output = outputer.outputer()

class spider(object):
    def run(self,url,html):
        if(not url.endswith(".php")):
            return False
        print("[WebShell check:]",url)
        output.add_list("[WebShell check:]","%s"%url)
        post_data = {}
        for _payload in payload:
            post_data[_payload] = 'echo "password is %s";'% _payload
            r = Downloader.post(url,post_data)
            if r :
                print("Webshell:%s" % r)
                output.add_list("Webshell:","%s"%r)
                return True
        return False
