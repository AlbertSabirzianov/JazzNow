import os

from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler

from parsers.butman_parser import ButmanParser
from parsers.esse_parser import EsseParser
from parsers.kozlov_parser import KozlovParser

load_dotenv()

updater = Updater(token=os.getenv('bot_token'))


def wake_up(update, context):
    hello_text = 'Вас приветствует бот JazzNow,' \
                 ' он расскажет о всех джазовых концертах сегодня в Москве!' \

    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup([
        [
            '/Kozlov',
            '/Esse',
            '/Butman',
        ]
    ],
        resize_keyboard=True
    )
    context.bot.send_message(
        chat_id=chat.id,
        text=hello_text,
        reply_markup=buttons,
    )


def butman(update,context):
    chat =update.effective_chat

    context.bot.send_message(
        chat_id=chat.id,
        text='Коллектив:\n' + ButmanParser.get_name_and_time()
    )

    context.bot.send_message(
        chat_id=chat.id,
        text='Описание:\n' + ButmanParser.get_about()
    )


def kozlov(update, context):
    chat = update.effective_chat

    context.bot.send_message(
        chat_id=chat.id,
        text='Бит:\n' + KozlovParser.get_bit()
    )

    context.bot.send_message(
        chat_id=chat.id,
        text='Матсарда:\n' + KozlovParser.get_mansard()
    )

    context.bot.send_message(
        chat_id=chat.id,
        text='Основная:\n' + KozlovParser.get_main()
    )

    context.bot.send_message(
        chat_id=chat.id,
        text='Мясницкая:\n' + KozlovParser.get_masnic()
    )


def esse(update, context):
    chat = update.effective_chat

    context.bot.send_message(
        chat_id=chat.id,
        text='Lab:\n' + EsseParser.get_lab()
    )

    context.bot.send_message(
        chat_id=chat.id,
        text="Основная:\n" + EsseParser.get_main()
    )


updater.dispatcher.add_handler(CommandHandler('Kozlov', kozlov))
updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(CommandHandler('Butman', butman))
updater.dispatcher.add_handler(CommandHandler('Esse', esse))

if __name__ == '__main__':
    updater.start_polling()
    updater.idle()
