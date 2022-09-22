import requests
import re, os

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def get_movie():
    response = requests.get(os.getenv('MOVIE_API'))
    return response.text


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please write /movie command for give you a recommendation")


async def movie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=get_movie())


def get_env():
    return os.getenv('SECRET_API_BOT')


if __name__ == '__main__':
    application = ApplicationBuilder().token(get_env()).build()

    start_handler = CommandHandler('start', start)
    movie_handler = CommandHandler('movie', movie)
    application.add_handler(start_handler)
    application.add_handler(movie_handler)

    application.run_polling()