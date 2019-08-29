from pyrogram import Client, Filters, Emoji
import random
import time

app = ("session",bot_token="820881097:AAHM0xwwTv1HVztMZ9PHLktj-2AAwBXZdVI",api_id=605563,api_hash="7f2c2d12880400b88764b9b304e14e0b") 


@app.on_message(Filters.command('ani'))
def ran(client, message):
  client.send_message(message.chat.id,message.reply_to_message.animation.file_id)

app.run()
