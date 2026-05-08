import logging
import random
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8713148639:AAGD66QtKBDbiIa8Np8F9mvaiFkOm1N06v8"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    name = update.effective_user.first_name
    await update.message.reply_text(
        "Bonjour " + name + " !\n\n"
        "/aide - Commandes\n"
        "/heure - Heure actuelle\n"
        "/alea - Nombre aleatoire\n"
        "/repete texte - Repeter un texte"
    )

async def aide(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Commandes disponibles:\n"
        "/start\n/aide\n/heure\n/alea\n/repete [texte]"
    )

async def heure(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    now = datetime.now().strftime("%H:%M:%S - %d/%m/%Y")
    await update.message.reply_text("Heure: " + now)

async def alea(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    nombre = random.randint(1, 100)
    await update.message.reply_text("Nombre: " + str(nombre))

async def repete(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        await update.message.reply_text(" ".join(context.args))
    else:
        await update.message.reply_text("Usage: /repete [texte]")

async def inconnu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Tapez /aide pour les commandes.")

def main() -> None:
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("aide", aide))
    app.add_handler(CommandHandler("heure", heure))
    app.add_handler(CommandHandler("alea", alea))
    app.add_handler(CommandHandler("repete", repete))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, inconnu))
    app.run_polling()

if __name__ == "__main__":
    main()

