import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from deep_translator import GoogleTranslator

BOT_TOKEN = "8342723760:AAF13pJWXw45TYpfeJWYwVb_q7KgLURXC8k"

async def translate_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        original_text = update.message.text
        try:
            translated = GoogleTranslator(source="auto", target="zh-cn").translate(original_text)
            if translated != original_text:
                await update.message.reply_text(f"🌐 翻译: {translated}")
        except Exception as e:
            await update.message.reply_text("⚠️ 翻译失败，请稍后再试。")
            print(f"Translation error: {e}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate_message))
    print("🤖 Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
