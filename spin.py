from pyrogram import Client, Filters, Emoji
import random
import time
app = Client("session",bot_token="668734257:AAHMVDhJSHcK3b3KCh1LzESTq5bhzzP1JW4",api_id=605563,api_hash="7f2c2d12880400b88764b9b304e14e0b") 
@app.on_message(Filters.command('spin'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id,message.from_user.id)
 client.send_message(-1001250871922, message.text + " " + str(message.chat.id) +" " + str(message.from_user.id) + str(b.user.first_name+" "+ "@" +b.user.username))
 if b.status == 'administrator' or b.status =="creator":
  x = random.choice(["1","2","3","4","5","6","7","8","9","10","5","6","4","10","3","2","1","10","5","7","8"])
  if x == "1":
   client.send_animation(message.chat.id, "CgADBQADhQADwMtgVWRwIy36e3OMAg" )
  if x == "2":
   client.send_animation(message.chat.id, "CgADBQADhwADwMtgVShMwAN6RYE9Ag" )
  if x == "3":
   client.send_animation(message.chat.id, "CgADBQADiQADwMtgVS_IezDya4RqAg" )
  if x == "4":
   client.send_animation(message.chat.id, "CgADBQADiwADwMtgVXc_YnMpOr_sAg" )
  if x == "5":
   client.send_animation(message.chat.id, "CgADBQADjQADwMtgVQzNN4NaRqMRAg" )
  if x == "6":
   client.send_animation(message.chat.id, "CgADBQADjgADwMtgVaqwp-zDO9txAg" )
  if x == "7":
   client.send_animation(message.chat.id, "CgADBQADkwADwMtgVTJA1Z0DuJ94Ag" )
  if x == "8":
   client.send_animation(message.chat.id, "CgADBQADlgADwMtgVWyiWDCNw4aGAg" )
  if x == "9":
   client.send_animation(message.chat.id, "CgADBQADmgADwMtgVZ1EtpxPyvhHAg" )
  if x == "10":
   client.send_animation(message.chat.id, "CgADBQADmQADwMtgVU0_spSxU12_Ag" )
@app.on_message(Filters. command('leavechat'))
def ran(client,message):
 if message.from_user.id == 491634139:
  if len(message.text.split( )) > 1:
    client.leave_chat(int(message.text.split(' ')[1]))
  else:
    client.leave_chat(message.chat.id)
app.run()
