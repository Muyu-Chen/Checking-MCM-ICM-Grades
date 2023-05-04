# -*- coding: gb2312
# from __future__ import unicode_literals
import requests
import fileinput
import time
import random


headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
def sumline():
    lineno=0
    fileinput.close()
    for line in fileinput.input(r'.\MyICMGrades.html'):
        lineno=fileinput.filelineno()
    return lineno
      
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
urltest='https://baidu.com'
while True:
    print('is running')
    YorNhave=requests.get(urlhave,headers=headers,timeout=5)
    print(YorNhave)
    if str(YorNhave)=='<Response [200]>':##判断网页是否通畅
        for i in range(5):
             time.sleep(110)
             time.sleep(20*random.random())
             res=requests.get(urliwant)
             print(res)
             if str(res)=='<Response [404]>':
                   notget()
                   time.sleep(110)
                   time.sleep(20*random.random())
             else:
                    haveget()
                    time.sleep(110)
                    time.sleep(20*random.random())
    else:
        interneterr()
        time.sleep(15)


'''
        , encoding="utf-8"
print(YorNhave)
print(res2)


for line in fileinput.input('data', backup='.bak',inplace = True):
    # 在指定行后添加一行
    if fileinput.lineno() == 1:
        print(line.rstrip())
        print('Hello world!')
    else:
        print(line.rstrip())






#response = requests.get('https://www.comap-math.com/mcm/2022Certs/2200368.pdf',verify=False)
#response.encoding = response.apparent_encoding
#print(response.text)
'''