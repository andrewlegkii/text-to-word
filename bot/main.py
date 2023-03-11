import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import docx

from dotenv import load_dotenv
load_dotenv()

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Добро пожаловать в бот Text-to-Word! Пожалуйста, отправьте мне текст, который вы хотите преобразовать.")

def convert_text_to_word(update, context):
    # Получаем текстовое сообщение от пользователя
    text = update.message.text

    # Создаем новый документ Word
    document = docx.Document()

    # Вставляем преобразованный текст в документ Word
    document.add_paragraph(text)

    # Сохраняем документ Word как файл
    document.save('output.docx')

    # Отправляем документ Word обратно пользователю
    context.bot.send_document(chat_id=update.effective_chat.id, document=open('output.docx', 'rb'))

def main():
    # Создаем Telegram-бота и добавляем обработчики команд и сообщений
    updater = Updater(token=os.getenv("TOKEN") , use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    convert_handler = MessageHandler(Filters.text & ~Filters.command, convert_text_to_word)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(convert_handler)

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
