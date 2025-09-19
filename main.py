import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from deep_translator import GoogleTranslator

# 🚨 推荐在 Railway 设置环境变量 BOT_TOKEN
BOT_TOKEN = os.getenv("BOT_TOKEN", "8416318151:AAGAs0i3NXVaJPFRT4tGsuLGDfwXJPFZDAU")

async def translate_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        original_text = update.message.text
        try:
            # 自动检测语言
            translator = GoogleTranslator(source="auto", target="zh-CN")
            translated = translator.translate(original_text)

            # 如果原文就是中文就不翻译
            if translated != original_text:
                await update.message.reply_text(f"🌐 翻译: {translated}")
        except Exception as e:
            await update.message.reply_text(f"⚠️ 翻译失败: {str(e)}")
            print(f"Translation error: {e}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate_message))
    print("🤖 Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
