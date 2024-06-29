# Readme

[中文版本](#自动检查美赛成绩是否发布)  

## Automatically Searching&Checking the Grades of COMAP MCM/ICM

GitHub Link: [Muyu-Chen/Checking-MCM-ICM-Grades(github.com)](https://github.com/Muyu-Chen/Checking-MCM-ICM-Grades)  
Direct access link: [Checking ICM/MCM Grades](http://47.109.109.48/gradecheck/MyICMGrades.html "CheckingICMGrades")  

## 1. Introduction

This program is written when I was waiting for the results of the MCM/ICM. There may some bugs due to the limitation of time. The principle and purpose：According to the previous certificate download address, infer this year's certificate download address, determine whether the web page exists (presence code: 200, absence code: 404) to determine whether the score is out, and synchronize the message to a web page (can be deployed on the server or run on your own computer). At the same time, in order to prevent the other party from prohibiting access, we used a fake HTTP header and randomly accessed the time. In addition, we also access a web page on the server (which is exsist) to determine whether it is prohibited to access (due to the excessive access frequency, it is prohibited), and we will update it to "network error" on the web page.  

If you want to see the effect directly, you can visit this [link](http://47.109.109.48/gradecheck/MyICMGrades.html "CheckingICMGrades"), which is updated every 20 minutes. 

## 2. deploy

## Generic steps

1. install Python (version 3.10 used by the author), and then install the libraries `requests`, `fileinput`, `time`, and `random`.  
   
   Revise 93th line of ".py" and 9th line of ".html" file：
   
   ```python
   urliwant='https://www.comap-math.com/mcm/2023Certs/2300368.pdf'
   ```
   
   ```HTML
   This is a web created by python to check grades of team #2300368 by visiting the <a href="https://www.comap-math.com/mcm/2023Certs/2300368.pdf" title="check grades of team #2300368" target="_blank">webpage</a> of download the ICM certification. The program will visit the website every 1190 to 1210 seconds and show the result on this page.
   ```
   
   Please modify all occurrences of "2300368" in the above code to your own MCM/ICM control number (you could replace all 2300368 into your control number), and change the numeric part of “2023Certs” of the link in the two codes to the current year (e.g., year 2025, then changes to 2025Cert).   
   
   **That is,** the global replacement 2300368 is your's MCM/ICM control number, and 2023 is replaced globally with the year of this year.

2. Depends on your computer's system, go to "On Linux" or "On Windows".  

## On Linux

1. In the Python file `MainProgram.py`, perform a batch replacement of all Windows-style current directory path markers "`.\`" with Unix-style path separators "`./`".  
2. Use `nohup python3 MainProgram.py` to run it in the background, even if you exit the terminal/SSH, the program will still run.  

### On Windows

1. Open "MainProgram.py", then open `MyICMGrades.html` to see the result. If you do not want see the command, change '.py' to '.pyw'.      


Besides GNU GENERAL PUBLIC LICENSE, I do not allow gitcode.com and its company to use and copy my code in any way.
    

## 自动检查美赛成绩是否发布

1. GitHub链接：[Muyu-Chen/Checking-MCM-ICM-Grades(github.com)](https://github.com/Muyu-Chen/Checking-MCM-ICM-Grades)  
   直接访问链接：[Checking ICM/MCM Grades](http://47.109.109.48/gradecheck/MyICMGrades.html "CheckingICMGrades")
   
   ## 1. 简介
   
   这个项目是我在等待美赛结果的时候写出来的，时间仓促，若有bug请友善提出。该项目原理与目的：根据以往证书下载地址推测出今年的证书下载地址，判断网页是否存在（存在代码：200，不存在代码：404）来判断成绩是否出来，并同步消息到一个网页（可在服务器上部署，也可在自己的电脑上运行）。与此同时，我们也会防止被对方禁止访问（由于访问频率过高，被对方禁止），因此使用了伪造的HTTP头部，并且随机了访问时间。此外，还访问了该服务器上的一个网页，用来判断是否被禁止访问（如被禁止，将显示403错误），我们将在网页上更新为“网络错误”。
   
   如果想直接看到效果，可以访问[这个链接](http://47.109.109.48/gradecheck/MyICMGrades.html "CheckingICMGrades")，这个链接每隔20分钟更新一次。
   
   ## 2. 部署
   
   ### 共有步骤
   
   1. 安装Python（作者使用的版本为3.10），随后安装库 `requests`、`fileinput`、`time` 和 `random`。  
      
      修改 ".py" 文件的第93行及 ".html" 文件的第9行代码如下：
      
      ```python
      urliwant='https://www.comap-math.com/mcm/2023Certs/2300368.pdf'
      ```
      
      ```HTML
      This is a web created by python to check grades of team #2300368 by visiting the <a href="https://www.comap-math.com/mcm/2023Certs/2300368.pdf" title="check grades of team #2300368" target="_blank">webpage</a> of download the ICM certification. The program will visit the website every 1190 to 1210 seconds and show the result on this page.
      ```
      
      请将上述代码中所有的 "2300368" 替换为您自己的MCM/ICM控制编号，同时将链接中 "2023Certs" 的年份部分数字改为当前年份（例如，如果是2025年，则改为2025Certs）。
      
      **也就是说**，全局替换2300368为你的MCM/ICM的控制号，全局替换2023为今年的年份。
   
   2. 根据你电脑的操作系统，选择以下合适的步骤。
   
   ### Linux操作系统
   
   1. 将Python文件 `MainProgram.py`中Windows风格的 "`.\`" 更改为 "`./`"，保证其可以在Linux上运行.
   2. 使用 `nohup python3 MainProgram.py` 来在后台运行此进程, 以便在关闭SSH等连接后仍然可以继续运行。
   
   ### Windows操作系统
   
   1. 打开 "MainProgram.py"，随后打开 `MyICMGrades.html`即可看见结果。如果你不想看见”黑框框“，将后缀 '.py' 改为 '.pyw' 即可。
      

   
   # 以及，给个star吧！！！
   
   # GIVE ME A STAR, PLS.
