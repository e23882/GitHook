import requests
import sys

def lineNotifyMessage(token, msg, url):
      headers = {
          "Authorization": "Bearer " + token, 
          "Content-Type" : "application/x-www-form-urlencoded"
      }
	
      payload = {'message': msg,  'imageThumbnail': url,'imageFullsize': url}
      r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
      return r.status_code
	

f = open("D:/NeverRemove.txt", "r",encoding="utf-8")
message = "Dear all,\n\nInvestment management system service will be rebooted in a few minutes, please save important data to avoid data loss.\nIf you have any questions, please feel free to contact me, thank you!\n\n128 Leo\n\nRegards,\n"

url = "https://e23882.github.io/img/maybe.PNG"
#url = "\\192.168.1.155\LeoShare\IMS"
# 修改為你的權杖內容
token = 'Za4VgqtRnC7IJqp8nbhTHAt5tprTmIczLSREKNC0Khd'
#chris 
#token = 'sou8AO9Af4SZvWXhESZV0NdyTBt2dEbuREqT4AwXhIH'

#lineNotifyMessage(token, message, url)
