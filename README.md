# Readme

### Searching&Checking the grades of COMAP MCM/ICM

GitHub链接/GitHub Link：[Muyu-Chen/Checking-MCM-ICM-Grades(github.com)](https://github.com/Muyu-Chen/Checking-MCM-ICM-Grades)  
直接访问链接/Direct access link：[CheckingICMGrades](http://47.109.109.48/gradecheck/MyICMGrades.html "CheckingICMGrades")  

## 1. 简介/Introduction

这个项目是我在等待美赛结果的时候写出来的，时间仓促，若有bug请友善提出。该项目原理与目的：根据以往证书下载地址推测出今年的证书下载地址，判断网页是否存在（存在代码：200，不存在代码：404）来判断成绩是否出来，并同步消息到一个网页（可在服务器上部署，也可在自己的电脑上运行）。与此同时，我们也会防止被对方禁止访问（由于访问频率过高，被对方禁止），因此使用了伪造的HTTP头部，并且随机了访问时间。此外，还访问了该服务器上的一个网页，用来判断是否被禁止访问（如被禁止，将显示403错误），我们将在网页上更新为“网络错误”。     

This program is written when I was waiting for the results of the MCM/ICM. There may some bugs due to the limitation of time. The principle and purpose：According to the previous certificate download address, infer this year's certificate download address, determine whether the web page exists (presence code: 200, absence code: 404) to determine whether the score is out, and synchronize the message to a web page (can be deployed on the server or run on your own computer). At the same time, in order to prevent the other party from prohibiting access, we used a fake HTTP header and randomly accessed the time. In addition, we also access a web page on the server (which is exsist) to determine whether it is prohibited to access (due to the excessive access frequency, it is prohibited), and we will update it to "network error" on the web page.  

如果想直接看到效果，可以访问[这个链接](http://47.109.109.48/gradecheck/MyICMGrades.html "CheckingICMGrades")，这个链接每隔20分钟更新一次。SSL证书是用的免费的自签名证书，所以会提示有安全风险，请放心使用。  

If you want to see the effect directly, you can visit this [link](http://47.109.109.48/gradecheck/MyICMGrades.html "CheckingICMGrades"), which is updated every 20 minutes. SSL certificate is a free self-signed certificate, so it will prompt security risks.Please use it with confidence.  

## 2. 部署/deploy    

## On Linux  

1. 修改".py"文件的所有路径的斜杠（源文件是基于Windows的）
2. 跳转到通用步骤部分

## Generic steps
首先，安装python（作者使用3.10），并安装requests、fileinput、time、random库.  

修改".py"文件的90行/ Revise 90th line of ".py" file：
```python
urliwant='https://www.comap-math.com/mcm/2023Certs/2300368.pdf'
```

与 “.html”文件第9行/ and 9th line of ".html" file：  

```HTML
This is a web created by python to check grades of team #2300368 by visiting the <a href="https://www.comap-math.com/mcm/2023Certs/2300368.pdf" title="check grades of team #2300368" target="_blank">webpage</a> of download the ICM certification. The program will visit the website every 1190 to 1210 seconds and show the result on this page.
```

请将上述代码中所有出现的“2300368”**修改为自己的美赛控制号**），并将两个代码中的链接的“2023Certs”中数字部分改为当年年份（例如2025年，则改为2025Certs）。  
也就是说，全局替换2300368为**你的**MCM/ICM的控制号，全局替换2023为**今年**的年份。  
运行MainProgram.py，随后打开MyICMGrades.html即可看见。  
用Linux？  用"nohup python3 MainProgram.py"在后台运行，即使退出终端/SSH，程序仍然会继续运行。  

Please modify all occurrences of "2300368" in the above code to your own MCM/ICM control number，and change the numeric part of “2023Certs” of the link in the two codes to the current year (e.g., year 2025, then changes to 2025Cert).  
That is, the global replacement 2300368 is your's MCM/ICM control number, and 2023 is replaced globally with the year of this year.
Open "MainProgram.py", then open MyICMGrades.html to see the result.  
On Linux？ Use "nohup python3 MainProgram.py" to run it in the background, even if you exit the terminal/SSH, the program will still run.

### 说明：

1. 如果你（您）有HTML基础，可以自行对HTML进行修饰与更改，如果没有，只需将上述文档以 **"右键->打开方式->选择其他应用->记事本"** 的方式打开并修改相应部分。 但请务必遵守[GPL开源协议(github.com)](https://github.com/Muyu-Chen/Checking-MCM-ICM-Grades/blob/main/LICENSE)。

2. 在打开python文件后，即可打开HTML文件，该网页设置为每1分钟自动刷新一次。若不想看见python的命令行窗口，则可以将”.py“后缀改为".pyw"。  If you do not want see the command, change '.py' to '.pyw'. 

3. 最后的最后，给个star吧！！！
