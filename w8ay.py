#-*- coding:utf-8 -*-

import sys
from lib.core import common,webdir,webcms,PortScan
from lib.core.Spider import SpiderMain

def main():
    root = "http://www.shiyanlou/"
    threadNum = 10
    #IP Ports Scan
    ip = common.gethostbyname(root)
    print("IP:",ip)
    print("Start Port Scan:")
    pp = PortScan.PortScan(ip)
    pp.work()
    #DIR Fuzz
    dd = webdir.webdir(root,threadNum)
    dd.work()
    dd.output()
    #webcms
    ww = webcms.webcms(root,threadNum)
    ww.run()
    #spider
    w8 = SpiderMain(root,threadNum)
    w8.craw()

if __name__ == '__main__':
    main()