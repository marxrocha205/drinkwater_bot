from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging
from datetime import datetime, timedelta
import time
import threading

# Configure o logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Token do bot (obtido do BotFather)
TOKEN = '7420233569:AAH1KyIZfWOypGAWmdxgONjPHGCU-DYiklU'

# Função que será chamada a cada 30 minutos
def send_message_every_30_minutes(context: CallbackContext):
    job = context.job
    context.bot.send_message(job.context, text='Beba Agua')

# Função inicial do bot
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Olá! Vou te lembrar de tomar agua a cada 30 minutos.')

    # Inicia o job que envia a mensagem a cada 30 minutos
    chat_id = update.message.chat_id
    context.job_queue.run_repeating(send_message_every_30_minutes, interval=1800, first=0, context=chat_id)

def main():
    # Cria o Updater e passa o token do bot
    updater = Updater(TOKEN)

    # Obtém o dispatcher para registrar os handlers
    dispatcher = updater.dispatcher

    # Adiciona o handler para o comando /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Inicia o bot
    updater.start_polling()

    # Mantém o bot rodando até que seja interrompido
    updater.idle()

if __name__ == '__main__':
    main()
#