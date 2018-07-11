from django.shortcuts import render
import time
import requests
import re
# Create your views here.
def login(request):
    ctime = int(time.time()*1000)
    base_url ='https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage&fun=new&lang=zh_CN&_='
    url = base_url.format(ctime)
    res = requests.get(url=url)
    result = re.findall('uuid = "(.*)";',res.text)
    print(result[0])
    print(res.text)
    return render(request,'login.html',{'qrcode':result[0]})
