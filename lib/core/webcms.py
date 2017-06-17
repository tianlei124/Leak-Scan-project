#-*- coding：utf-8 -*-

import json,os,sys,hashlib,threading
import queue
from lib.core import Downloader,outputer

output = outputer.outputer()
class webcms(object):
    workqueue = queue.Queue()
    URL = ""
    threadNum = 0
    notFound =True
    downloader = Downloader.Downloader()
    result = ""

    def __init__(self,url,threadNum = 10):
        self.URL = url
        self.threadNum = threadNum
        filename = os.path.join(sys.path[0],"data","data.json")
        fp = open(filename,'r',encoding="utf-8")
        webdata = json.load(fp)
        
        for i in webdata:
            self.workqueue.put(i)
        fp.close()

    def getmd5(self,body):
        m2 = hashlib.md5()
        m2.update(body)
        return m2.hexdigest()
    
    def th_whatweb(self):
        if(self.workqueue.empty()):
            self.notFound = False
            return False
        if(self.notFound is False):
            return False

        cms = self.workqueue.get()
        _url = self.URL + cms["url"]
        html = self.downloader.get(_url)
        print("[Whatweb log]:checking %s" % _url)
        output.add_list("[Whatweb log]:","checking %s" % _url)

        if(html is None):
            return False
        if cms["re"]:
            if(html.find(cms["re"])!=1):
                self.result = cms["name"]
                self.notFound = False
                return True
        else:
            md5 = self.getmd5(html)
            if(md5 == cms["md5"]):
                self.result = cms["name"]
                self.notFound = False
                return True
    
    def run(self):
        while(self.notFound):
            th = []

            for i in range(self.threadNum):
                t = threading.Thread(target=self.th_whatweb)
                t.start()
                th.append(t)
            
            for t in th:
                t.join()
            
            if(self.result):
                print("[webcms]:%s cms is %s"%(self.URL,self.result))
                output.add_list("[webcms]:","%s cms is %s"%(self.URL,self.result))
            else:
                print("[webcms]:%s is notFound!"%self.URL)
                output.add_list("[webcms]:","%s is notFound!"%self.URL)