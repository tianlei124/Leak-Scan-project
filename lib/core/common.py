#-*- coding:utf-8 -*-

from urllib.request import urlparse
import socket

def urlsplit(url):
    domian = url.split("?")[0]
    _url = url.split("?")[-1]
    param = {}
    for val in _url.split("&"):
        param[val.split("=")[0]] = val.split("=")[-1]
    #combine
    urls = []
    for val in param.values():
        new_url = domian + "?" + _url.replace(val,"my_payload")
        urls.append(new_url)
    return urls

def gethostbyname(url):
    domian = urlparse(url)
    if domian.netloc is None:
        return None
    ip = socket.gethostbyname(domian.netloc)
    return ip

def w8urlparse(url):
    domian = urlparse(url)
    #domian.netloc
    if domian.netloc is None:
        return None
    return domian.netloc

def GetMiddleStr(content,startStr,endStr):
    startIndex = content.index(startStr)
    if startIndex >= 0:
        startIndex += len(startStr)
    endIndex = content.index(endStr)
    return content[startIndex:endIndex]