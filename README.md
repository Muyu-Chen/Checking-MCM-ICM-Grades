# Readme

这是一个由中文写的帮助文档，一切有争议的地方以中文文档为准。  

如果想直接看到效果，可以访问[这个链接](https://muyuchen.one:20056/MyICMGrades.html "CheakingICMGrades")，这个链接每隔2分钟更新一次。由于作者经济拮据，SSL证书是用的免费的自签名证书，所以会提示有安全风险。但是请不要怕，这个网站的源代码已经开源了，也没有任何”后端“可以收集隐私数据，请放心使用。

### 自行修改部分（重要！）：

".py"文件的90行：

```python
urliwant='https://www.comap-math.com/mcm/2023Certs/2300368.pdf'
```

“.html”文件第9行：

```HTML
This is a web created by python to cheak grades of team #2300368 by visiting the <a href="https://www.comap-math.com/mcm/2023Certs/2300368.pdf" title="cheak grades of team #2300368" target="_blank">webpage</a> of download the ICM certification. The program will visit the website every 110 to 130 seconds and show the result on this page.
```

请将上述代码中所有出现的“2300368”修改为自己的美赛控制号。若年份不是2023年（以防2023年后也有人使用），请将两个代码中的链接的“2023Certs”中数字部分改为当年年份。  

### 说明：

1. 如果你（您）有HTML基础，可以自行对HTML进行修饰与更改，如果没有，只需将上述文档以 **"右键->打开方式->选择其他应用->记事本"** 的方式打开并修改相应部分。 但请务必遵守[GPL开源协议(github.com)](https://github.com/Dengwen-Fu/Cheaking-MCM-ICM-Grades/blob/main/LICENSE)。

2. 在打开python文件后，即可打开HTML文件，该网页设置为每5分钟自动刷新一次。若不想看见python的命令行窗口，则可以将”.py“后缀改为”.pyw“。

3. 最后的最后，给个star吧！！！


