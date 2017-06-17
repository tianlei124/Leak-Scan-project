#-*- coding:utf-8 -*-

import sys
from lib.core import common,webdir,webcms,PortScan,fun_until,outputer
from lib.core.Spider import SpiderMain

def main():
    root = "http://www.shiyanlou.com/"
    threadNum = 10
    domain = common.w8urlparse(root)
    output = outputer.outputer()
    #CDN check
    print("CDN check...")
    msg,iscdn = fun_until.checkCDN(root)
    output.add("cdn",msg)
    #print(msg)
    if iscdn:
        #IP Ports Scan
        ip = common.gethostbyname(root)
        print("IP:",ip)
        print("Start Port Scan:")
        pp = PortScan.PortScan(ip)
        pp.work()
        output.build_html(domain)
    #DIR Fuzz
    dd = webdir.webdir(root,threadNum)
    dd.work()
    dd.output()
    output.build_html(domain)
    #webcms
    ww = webcms.webcms(root,threadNum)
    ww.run()
    output.build_html(domain)
    #spider
    w8 = SpiderMain(root,threadNum)
    w8.craw()

if __name__ == '__main__':
    main()