import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

emoji_calisan = []

anlik_calisan = []

tekli_calisan = []

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global emoji_calisan
  emoji_calisan.remove(event.chat_id)



@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**Merhaba ❤️**\n\n ● Grubunuzdaki nerdeyse tüm kullanıcılara etiket atabilirim beni grubunuza ekleyip yetki vermeniz gerekir . . . \n\n● komutlar icin  ➪  /help  yazmanız yeterlidir  . . .",
                    buttons=(
                   
		      [Button.url('𝗕𝗲𝗻𝗶 𝗚𝗿𝘂𝗯𝗮 𝗘𝗸𝗹𝗲  ❤️', 'https://t.me/StarTaggerBot?startgroup=a')],
        [Button.url('𝗕𝗶𝗹𝗴𝗶 𝗞𝗮𝗻𝗮𝗹𝗶  💬',  'https://t.me/StarBotKanal')], [Button.url('𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿  🤠', 'https://t.me/ByWolk')],
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**🇹🇷 StarTaggerBot Komutları**\n\n**/utag <sebeb> - Grubtaki kullanıcılara 5-li Etiket Atar...**\n\n**/tag <sebeb> - Grubtaki kullanıcıları Tek Tek Etiketler...**\n\n**/cancel - etiketleme işlemini durdurur...**"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('𝗕𝗲𝗻𝗶 𝗚𝗿𝘂𝗯𝗮 𝗘𝗸𝗹𝗲  ❤️', 'https://t.me/StarTagBot?startgroup=a')],  
 [Button.url('𝗕𝗶𝗹𝗴𝗶 𝗞𝗮𝗻𝗮𝗹𝗶  💬',  'https://t.me/StarBotKanal')], [Button.url('𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿  🤠', 'https://t.me/ByWolk')],
                    ),
                    link_preview=False
                   )
	
@client.on(events.NewMessage(pattern="^/reklam$"))
async def help(event):
  helptext = "**Bir çok özelliğe sahip , Etiket Botu Bulmaya Çalışan Grub Sahibleri : @StarTaggerBot Tam Size Göre:\n\n✵ 5-li etiket atabilir\n✵ Tekli Etiket atabilir\n✵ Yalnızca Yöneticilere etiket atabilir\n\n ✵Bir cok ozellige sahip @StarTaggerBot 'u grubunuza yönetici olarak ekleyip rahatlıkla üyelere , etiket ata bilirsiz. **"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('𝗕𝗼𝘁𝘂 𝗚𝗿𝘂𝗯𝗮 𝗘𝗸𝗹𝗲 ❤️', 'https://t.me/startaggerbot?startgroup=a')],
                    ),
                    link_preview=False
                   )
	
	

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global emoji_calisan
  emoji_calisan.remove(event.chat_id)


emoji = " ❤️ 🧡 💛 💚 💙 💜 🖤 🤍 🤎 🙂 🙃 😉 😌 😍 🥰 😘 😗 😙 😚 😋 😛 😝 😜 🤪 🤨 🧐 🤓 😎 🤩 🥳 😏 😒 " \
        "😞 😔 😟 😕 🙁 😣 😖 😫 😩 🥺 😢 😭 😤 😠 😡  🤯 😳 🥵 🥶 😱 😨 😰 😥 😓 🤗 🤔 🤭 🤫 🤥 😶 😐 😑 😬 🙄 " \
        "😯 😦 😧 😮 😲 🥱 😴 🤤 😪 😵 🤐 🥴 🤢 🤮 🤧 😷 🤒 🤕 🤑 🤠 😈 👿 👹 👺 🤡  👻 💀 👽 👾 🤖 🎃 😺 😸 😹 " \
        "😻 😼 😽 🙀 😿 😾 🔞 🌹 ".split (" ")


@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def mentionall(event):
  global emoji_calisan
  if event.is_private:
    return await event.respond("**Bu komutu gruplar ve kanallar için geçerli**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadace yoneticiler kullana bilir😐**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Geçmiş mesajlar için etiket ede bilmiom**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("𝖤𝗍𝗂𝗄𝖾𝗍 𝗒𝖺𝗉𝗆𝖺𝗄 𝗂𝖼𝗂𝗇 𝗌𝖾𝖻𝖾𝗉 𝗒𝗈𝗄")
  else:
    return await event.respond("**𝖤𝗍𝗂𝗄𝖾𝗍𝖾 𝖻𝖺𝗌𝗅𝖺𝗆𝖺𝗄 sebep 𝗂𝖼𝗂𝗇 𝗒𝖺𝗓𝗂𝗇...!**")
  
  if mode == "text_on_cmd":
    emoji_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in emoji_calisan:
        await event.respond("** 𝖤𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂 𝖻𝖺𝗌𝖺𝗋𝗂𝗒𝗅𝖺 𝖽𝗎𝗋𝖽𝗎𝗋𝗎𝗅𝖽𝗎 **")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    emoji_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in emoji_calisan:
        await event.respond("𝖤𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂 𝖻𝖺𝗌𝖺𝗋𝗂𝗒𝗅𝖺 𝖽𝗎𝗋𝖽𝗎𝗋𝗎𝗅𝖽𝗎... \n\n**🤠𝖣𝗂𝗅𝖾𝗋𝗌𝖾𝗇𝗂𝗓 𝖻𝗎𝗋𝖺𝖽𝖺 𝗌𝗂𝗓𝗂𝗇 𝗋𝖾𝗄𝗅𝖺𝗆𝗂𝗇𝗂𝗓 𝗈𝗅𝖺𝖻𝗂𝗅𝗂𝗋... \n[ @StarBotKanal ]**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global emoji_calisan
  emoji_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("Bu komutu gruplar ve kanallar için geçerli")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadace yoneticiler kullana bilir😐**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Önceki Mesajlara Cevab Vermeyin")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("𝖤𝗍𝗂𝗄𝖾𝗍 𝗂𝗌𝗅𝖾𝗆𝗂𝗇𝗂 𝖻𝖺𝗌𝗅𝖺𝗍𝗆𝖺𝗄 𝗂𝖼𝗂𝗇 𝗌𝖾𝖻𝖾𝗉 𝗒𝗈𝗄 ")
  else:
    return await event.respond("𝖤𝗍𝗂𝗄𝖾𝗍 𝗂𝗌𝗅𝖾𝗆𝗂𝗇𝗂 𝖻𝖺𝗌𝗅𝖺𝗍𝗆𝖺𝗄 𝗂𝖼𝗂𝗇 𝗌𝖾𝖻𝖾𝗉 𝗒𝗈𝗄")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"👥 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("𝖤𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂 𝖻𝖺𝗌𝖺𝗋𝗂𝗒𝗅𝖺 𝖽𝗎𝗋𝖽𝗎𝗋𝗎𝗅𝖽𝗎... \n\n**🤠𝖣𝗂𝗅𝖾𝗋𝗌𝖾𝗇𝗂𝗓 𝖻𝗎𝗋𝖺𝖽𝖺 𝗌𝗂𝗓𝗂𝗇 𝗋𝖾𝗄𝗅𝖺𝗆𝗂𝗇𝗂𝗓 𝗈𝗅𝖺𝖻𝗂𝗅𝗂𝗋... \n[ @StarBotKanal ]**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"👥 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("𝖤𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂 𝖻𝖺𝗌𝖺𝗋𝗂𝗒𝗅𝖺 𝖽𝗎𝗋𝖽𝗎𝗋𝗎𝗅𝖽𝗎 🤠")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**Bu komutu gruplar ve kanallar için geçerli**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadace yoneticiler kullana bilir😐**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**önceki mesajı etiketleye bilmerim*")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("𝖤𝗍𝗂𝗄𝖾𝗍 𝗂𝗌𝗅𝖾𝗆𝗂𝗇𝖾 𝖻𝖺𝗌𝗅𝖺𝗆𝖺𝗄 𝗂𝖼𝗂𝗇 <𝗌𝖾𝖻𝖾𝗉> 𝗀𝗂𝗋𝗂𝗇 ...")
  else:
    return await event.respond("**𝖤𝗍𝗂𝗄𝖾𝗍 𝗂𝗌𝗅𝖾𝗆𝗂𝗇𝖾 𝖻𝖺𝗌𝗅𝖺𝗆𝖺𝗄 𝗂𝖼𝗂𝗇 <𝗌𝖾𝖻𝖾𝗉> 𝗀𝗂𝗋𝗂𝗇 ... **")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**👤 - [{usr.first_name}](tg://user?id={usr.id}) \n**"
      if event.chat_id not in tekli_calisan:
        await event.respond("**𝖤𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂 𝖻𝖺𝗌𝖺𝗋𝗂𝗒𝗅𝖺 𝖽𝗎𝗋𝖽𝗎𝗋𝗎𝗅𝖽𝗎... \n\n**🤠𝖣𝗂𝗅𝖾𝗋𝗌𝖾𝗇𝗂𝗓 𝖻𝗎𝗋𝖺𝖽𝖺 𝗌𝗂𝗓𝗂𝗇 𝗋𝖾𝗄𝗅𝖺𝗆𝗂𝗇𝗂𝗓 𝗈𝗅𝖺𝖻𝗂𝗅𝗂𝗋... \n[ @StarBotKanal ]**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"👤 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("𝖤𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂 𝖻𝖺𝗌𝖺𝗋𝗂𝗒𝗅𝖺 𝖽𝗎𝗋𝖽𝗎𝗋𝗎𝗅𝖽𝗎... \n\n**🤠𝖣𝗂𝗅𝖾𝗋𝗌𝖾𝗇𝗂𝗓 𝖻𝗎𝗋𝖺𝖽𝖺 𝗌𝗂𝗓𝗂𝗇 𝗋𝖾𝗄𝗅𝖺𝗆𝗂𝗇𝗂𝗓 𝗈𝗅𝖺𝖻𝗂𝗅𝗂𝗋... \n[ @StarBotKanal ]**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	


@client.on(events.NewMessage(pattern="^/admintag ?(.*)"))
async def mentionall(tagadmin):

	if admintag.pattern_match.group(1):
		seasons = admintag.pattern_match.group(1)
	else:
		seasons = ""

	chat = await admintag.get_input_chat()
	a_=0
	await admintag.delete()
	async for i in client.iter_participants(chat, filter=cp):
		if a_ == 500:
			break
		a_+=5
		await admintag.client.send_message(admintag.chat_id, "**[{}](tg://user?id={}) {}**".format(i.first_name, i.id, seasons))
		sleep(0.5)


print(">> 𝖡𝗈𝗍 𝖼𝖺𝗅𝗂𝗌𝗂𝗒𝗈𝗋 𝗌𝖺𝗄𝗂𝗇 𝗈𝗅 𝖽𝗈𝗌𝗍𝗎𝗆 😃 @StarBotKanal bilgi alabilirsin <<")
client.run_until_disconnected()
