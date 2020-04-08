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
	

f = open("D:/NeverRemove.txt", "r")
message = "更新內容 : \n"+f.read()+"\n程式下載位置 : "+r"\\192.168.1.155\LeoShare\IMS"

url = "https://e23882.github.io/img/maybe.PNG"
#url = "\\192.168.1.155\LeoShare\IMS"
# 修改為你的權杖內容
token = 'YourLineNotifyKey'


lineNotifyMessage(token, message, url)
