# -*- coding: utf-8 -*-
import json
from email.mime.text import MIMEText
import smtplib


# Account infomation load
gmailUser = 'yourmail@domain.com'
gmailPasswd = 'yourpassword'
to = ['user001@domain.com','user002@domain.com']

# Read git message
f = open("D:/NeverRemove.txt", "r", encoding='utf-8')
# content = f.read()
# f.close()


# Create message
emails = [t.split(',') for t in to]
message = MIMEText('Dear all,\n\nXXXX服務已經重新啟動，\n\n如果有任何問題需要協助歡迎隨時與我聯繫，感謝!\n\n128 Leo\n\nRegards,\n', 'plain', 'utf-8')
message['Subject'] = 'XX系統更新'
message['From'] = gmailUser
message['To'] = ','.join(to)

# Set smtp
smtp = smtplib.SMTP("mailservice:port")
smtp.ehlo()
smtp.starttls()
smtp.login(gmailUser, gmailPasswd)

# Send msil
smtp.sendmail(message['From'], message['To'], message.as_string())
print('Send mails OK!')