from pyrogram import Client, Filters, Emoji
import random
import time
app = Client("session",bot_token="663574960:AAGWg1VGruCPuckHzjbpDLRIbPWkX6YcDlc",api_id=605563,api_hash="7f2c2d12880400b88764b9b304e14e0b")  
@app.on_message(Filters.group)
def ran(client, message):
 if not message.from_user:
  message.delete(message.message_id)
app.run()
