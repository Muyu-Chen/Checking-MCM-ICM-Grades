# Readme

#### Searching&Checking the grades of MCM/ICM

GitHub链接：[Dengwen-Fu/Checking-MCM-ICM-Grades(github.com)](https://github.com/Dengwen-Fu/Cheaking-MCM-ICM-Grades)  
直接访问链接：[CheckingICMGrades](https://muyuchen.one:20056/MyICMGrades.html "CheakingICMGrades")  

这个项目是我在等待美赛结果的时候写出来的，时间仓促，若有bug请友善提出。该项目原理与目的：根据以往证书下载地址推测出今年的证书下载地址，判断网页是否存在（存在代码：200，不存在代码：404）来判断成绩是否出来，并同步消息到一个网页（可在服务器上部署，也可在自己的电脑上运行）。    

The purpose：According to the previous certificate download address, infer this year's certificate download address, determine whether the web page exists (presence code: 200, absence code: 404) to determine whether the score is out, and synchronize the message to a web page (can be deployed on the server or run on your own computer).    

如果想直接看到效果，可以访问[这个链接](https://muyuchen.one:20056/MyICMGrades.html "CheckingICMGrades")，这个链接每隔2分钟更新一次。由于作者经济拮据，服务器只有公网动态IPv6（运营商免费提供），所以需要使用者**具备IPv6网络环境**（使用4G或5G是一定有的），SSL证书是用的免费的自签名证书，所以会提示有安全风险。但是请不要怕，这个网站的源代码已经开源了，也没有任何”后端“可以收集隐私数据，请放心使用。  

If you want to see the effect directly, you can visit this [link](https://muyuchen.one:20056/MyICMGrades.html "CheckingICMGrades"), which is updated every 2 minutes. Due to the author's financial constraints, the server only has public network dynamic IPv6 (provided by operators for free), so **users need to have an IPv6 network environment** (if you are not sure about this, you can use 4G or 5G), SSL certificate is a free self-signed certificate, so it will prompt security risks. But don't be afraid, the source code of this website is already open source, and there is no "backend" to collect private data, please use it with confidence.  

### 自行部署时源码需修改部分（重要！）：

".py"文件的90行：  

```python
urliwant='https://www.comap-math.com/mcm/2023Certs/2300368.pdf'
```

“.html”文件第9行：  

```HTML
This is a web created by python to cheak grades of team #2300368 by visiting the <a href="https://www.comap-math.com/mcm/2023Certs/2300368.pdf" title="cheak grades of team #2300368" target="_blank">webpage</a> of download the ICM certification. The program will visit the website every 110 to 130 seconds and show the result on this page.
```

请将上述代码中所有出现的“2300368”**修改为自己的美赛控制号**。若年份不是2023年（以防2023年后也有人使用），请将两个代码中的链接的“2023Certs”中数字部分改为当年年份。  

Please modify all occurrences of "2300368" in the above code to your own MCM/ICM control number. If the year is not 2023 (in case it is also used after 2023), change the numeric part of “2023Certs” of the link in the two codes to the current year.  

### 说明：

1. 如果你（您）有HTML基础，可以自行对HTML进行修饰与更改，如果没有，只需将上述文档以 **"右键->打开方式->选择其他应用->记事本"** 的方式打开并修改相应部分。 但请务必遵守[GPL开源协议(github.com)](https://github.com/Dengwen-Fu/Cheaking-MCM-ICM-Grades/blob/main/LICENSE)。

2. 在打开python文件后，即可打开HTML文件，该网页设置为每1分钟自动刷新一次。若不想看见python的命令行窗口，则可以将”.py“后缀改为”.pyw“。

3. 最后的最后，给个star吧！！！
