import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8713148639:AAGD66QtKBDbiIa8Np8F9mvaiFkOm1N06v8"

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(f"👋 Bonjour {user.first_name} !\n\n/aide - Commandes\n/heure - Heure\n/alea - Nombre aléatoire\n/repete [texte] - Répéter")

async def aide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📋 Commandes :\n/start\n/aide\n/heure\n/alea\n/repete [texte]")

async def heure(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from datetime import datetime
    await update.message.reply_text(f"🕐 {datetime.now().strftime('%H:%M:%S - %d/%m/%Y')}")

async def alea(update: Update, context: ContextTypes.DEFAULT_TYPE):
    import random
    await update.message.reply_text(f"🎲 {random.randint(1, 100)}")

async def repete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        await update.message.reply_text("🔁 " + " ".join(context.args))
    else:
        await update.message.reply_text("Usage : /repete [texte]")

async def inconnu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tapez /aide pour les commandes.")

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("aide", aide))
    app.add_handler(CommandHandler("heure", heure))
    app.add_handler(CommandHandler("alea", alea))
    app.add_handler(CommandHandler("repete", repete))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, inconnu))
    app.run_polling()
