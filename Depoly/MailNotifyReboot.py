# -*- coding: utf-8 -*-
import json
from email.mime.text import MIMEText
import smtplib
import time

# Account infomation load
gmailUser = 'yourmail'
gmailPasswd = 'yourpassword'

to = ['user']

# Create message
emails = [t.split(',') for t in to]
message = MIMEText('Dear all,\n\nXXX系統服務將在三分鐘內重新啟動，請盡快將正在操作的資料儲存避免資料遺失。\n如果有任何問題需要協助請隨時與我聯繫，感謝 !\n\n128 Leo\n\nRegards,\n', 'plain', 'utf-8')
message['Subject'] = 'XX系統更新'
message['From'] = gmailUser
message['To'] = ','.join(to)

# Set smtp
smtp = smtplib.SMTP("MailService:Port")
smtp.ehlo()
smtp.starttls()
smtp.login(gmailUser, gmailPasswd)

# Send msil
smtp.sendmail(message['From'], message['To'], message.as_string())
print('Send mails OK!')

time.sleep(180- ((time.time() - starttime) % 180))