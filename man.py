from pyrogram import Client, Filters
from pyrogram.errors import FloodWait
import time
app = Client("mxx",870831,"115641a0211dbd60dfdce6f367010e5f")
d = -1001274887387
@app.on_message(Filters.command("clear"))
def forward(client, message):
 with open("sure.txt" , "w") as file:
  file.write("001 002")
  file.close()
  message.reply("ok")
@app.on_message(Filters.command("set"))
def forward(client, message):
 with open("source.txt" , "w") as file:
  file.write(message.text.split(' ')[1])
  file.close()
  message.reply("ok")
@app.on_message( Filters.text & ~Filters.edited)
def forward(client, message):
 fil = open("source.txt" , "r")
 lins = fil.readlines()
 fil.close()
 for t in lins:
  if int(t) == message.chat.id:
   text = message.text
   f = False
   words = ["kab","mani"," id","स",'dekho',"TRUST",'fix','😱','😳','👆','👇','match','pass','chase','defend','Surendra','karva','link','loss','audio','varna','open','paid','contact','baazigar','market','load','whatsapp','book','teen','diya','bhai',"🐴",'🥺','🖕','member','only','chut','lund','gand','ma ','maa ','bhosdi','bahan','loude','lode','lavde','chutiya','☝️','mkc','bc','madarchod','bahanchod','gandu','❓','kya','line',"https://",'bullet','🤔','LUND',"WICKET LU","?","loda","lode","lodu","telegram","chor","join"]
   for word in words:
    if word.casefold() in text.casefold():
     f = True
   if not f:
    mes = client.send_message(d, "<b>" + message.text.replace("TRINBAGO","TRIBAGO") + "</b>", parse_mode="html" )
    files = open("sure.txt" , "a")
    files.write(" " + str(message.message_id) +  " " + str(mes.message_id))
    files.close()  
@app.on_message( Filters.text & Filters.edited)
def forward(client, message):
 fil = open("source.txt" , "r")
 lins = fil.readlines()
 fil.close()
 for t in lins:
  if int(t) == message.chat.id:
   file = open("sure.txt" , "r")
   lines = file.readlines()
   file.close()
   for line in lines:
    x = line.split()
    id = str(message.message_id)
    if id in x:
     try:
      client.edit_message_text(d,int(x[x.index(id)+1]),"<b>" + message.text.replace("TRINBAGO","TRIBAGO") + "</b>", parse_mode="html" )
     except FloodWait as e:
      time.sleep(e.x)
app.run()
