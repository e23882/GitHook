from retry import retry
import smtplib 
from email.mime.text import MIMEText 

@retry()
def sendMail():
    f = open("D:/NeverRemove.txt", "r")
    #print(f.read())
    gmail_user = 'e23882@gmail.com'
    gmail_password = '1j4y94cj' 

    msg = MIMEText('content')
    msg['Subject'] = 'IMS Update'
    msg['Content'] = f.read()
    msg['From'] = gmail_user
    msg['To'] = 'leoyang@jepun.com.tw'

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.send_message(msg)
    server.quit()
    
sendMail()
print('Email sent!')