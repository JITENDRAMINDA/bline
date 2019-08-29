from pyrogram import Client, Filters, Emoji
import random
import time

app = Client("session",bot_token="820881097:AAHM0xwwTv1HVztMZ9PHLktj-2AAwBXZdVI",api_id=605563,api_hash="7f2c2d12880400b88764b9b304e14e0b") 

 

@app.on_message(Filters.command('ani'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id,message.from_user.id)
 if b.status == 'administrator' or b.status =="creator":
  z = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","0","20","25","13","15","9","23","11","22","19","16","7","8","6","23","25","28","32","30","31")
  x = random.choice(z)
  if x == "0":
   client.send_animation(message.chat.id, "CgADBQADlgADFRDAVS4QNlZj7e0GAg" )
  if x == "1":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "2":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "3":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "4":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "5":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "6":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "7":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "8":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "9":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "10":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "11":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "12":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "13":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "14":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "15":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "16":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "17":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "18":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "19":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "20":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "21":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "22":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "23":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "24":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "25":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "26":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "27":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "28":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "29":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "30":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "31":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )
  if x == "32":
   client.send_animation(message.chat.id, " CgADBQADlgADFRDAVS4QNlZj7e0GAg " )

app.run()
