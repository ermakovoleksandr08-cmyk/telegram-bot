from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["👤 Профиль", "⚙️ Настройки"],
        ["ℹ️ Информация", "🆘 Помощь"]
    ]
    await update.message.reply_text(
        "⚡ Добро пожаловать в NEXORA!",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "👤 Профиль":
        await update.message.reply_text("Твой профиль NEXORA")
    elif text == "⚙️ Настройки":
        await update.message.reply_text("Настройки NEXORA")
    elif text == "ℹ️ Информация":
        await update.message.reply_text("NEXORA — Telegram Bot")
    elif text == "🆘 Помощь":
        await update.message.reply_text("Напиши /start для открытия меню")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buttons))
app.run_polling()
