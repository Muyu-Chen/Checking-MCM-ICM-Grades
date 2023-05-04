# -*- coding: gb2312
# from __future__ import unicode_literals
import requests
import fileinput
import time
import random

requests.adapters.DEFAULT_RETRIES = 5
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36','Connection':'close'
}

##The following function can be used to delete when the number of rows is too large.
def sumline():
    lineno=0
    fileinput.close()
    for line in fileinput.input(r'.\MyICMGrades.html'):
        lineno=fileinput.filelineno()
    return lineno
      
##The following three functions are written to HTML to achieve visual purposes.
def notget():
    print('notget is running')
    fileinput.close()
    with fileinput.FileInput(files='.\MyICMGrades.html',backup='.bak',inplace = True) as f:
          for line in f:
             if f.lineno() == 41:
                 nowtime=str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
                 print(line.rstrip())
                 print('<tr>')
                 print('<th style="font-size:31px">',end="")
                 print(nowtime,end="")
                 print('</th>')
                 print('<th style="font-size:31px">',end="")
                 print('Response [404]',end="")
                 print('</th>')
                 print('<th style="font-size:31px">',end="")
                 print('there is no grade',end="")
                 print('</th>')
                 print('</tr>')
                 print()
             else:
                 print(line.rstrip())
          fileinput.close()

def haveget():
    print('haveget is running')
    fileinput.close()
    with fileinput.input(files='.\MyICMGrades.html',openhook=fileinput.hook_encoded('utf-8', ''),backup='.bak',inplace = True) as f:
          for line in f:
             if f.lineno() == 41:
                 nowtime=str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
                 print(line.rstrip())
                 print('<tr>')
                 print('<th style="font-size:31px">',end="")
                 print(nowtime,end="")
                 print('</th>')
                 print('<th style="font-size:31px">',end="")
                 print('Response [200]',end="")
                 print('</th>')
                 print('<th style="font-size:40px">',end="")
                 print('have grades!',end="")
                 print('</th>')
                 print('</tr>')
                 print()
             else:
                 print(line.rstrip())

def interneterr():
    print('interneterr is running')
    fileinput.close()
    with fileinput.input(files='.\MyICMGrades.html',openhook=fileinput.hook_encoded('utf-8', ''),backup='.bak',inplace = True) as f:
          for line in f:
             if f.lineno() == 41:
                 nowtime=str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
                 print(line.rstrip())
                 print('<tr>')
                 print('<th style="font-size:31px">',end="")
                 print(nowtime,end="")
                 print('</th>')
                 print('<th style="font-size:31px">',end="")
                 print('Response [404]',end="")
                 print('</th>')
                 print('<th style="font-size:31px">',end="")
                 print('internet error',end="")
                 print('</th>')
                 print('</tr>')
                 print()
             else:
                 print(line.rstrip())

urlhave='https://www.contest.comap.com/Certform/index.html'
urliwant='https://www.comap-math.com/mcm/2023Certs/2300368.pdf'

while True:
    print('is running')
    YorNhave=requests.get(urlhave,headers=headers,timeout=10)
    print(YorNhave)
    YorNhave.close
    if str(YorNhave)=='<Response [200]>':##Determine whether the network is unobstructed
        print('is running 2')
        for i in range(5):
             res=requests.get(urliwant,timeout=20)
             print(res)
             res.keep_alive = False
             res.close
             if str(res)=='<Response [404]>':
             ##Check whether it can be downloaded according to the team control number, and if it returns 404 (Page not found), it is not available for download.
                   notget()
                   print('notget is finished, then will sleep about 2 mins')
                   time.sleep(110)
                   time.sleep(20*random.random())
                   print('awake')
             else:
                    haveget()
                    time.sleep(110)
                    time.sleep(20*random.random())
    else:
        interneterr()
        time.sleep(15)
