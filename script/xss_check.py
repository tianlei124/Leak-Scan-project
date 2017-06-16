#-*- coding:utf-8 -*-

from lib.core import Downloader,common
import sys,os

payload = []
filename = os.path.join(sys.path[0],"data","xss.txt")
f = open(filename,'r')
for i in f:
    payload.append(i.strip())

class spider(object):
    def run(self,url,html):
        downloader = Downloader.Downloader()
        urls = common.urlsplit(url)

        if urls is None:
            return False
        for _urlp in urls:
            for _payload in payload:
                _url = _urlp.replace("my_Payload",_payload)
                print("[xss test]:",_url)
                _str = downloader.get(_url)
                if _str is None:
                    return False
                if (_str.find(_payload) != -1):
                    print("xss found:%s" % url)
        return False