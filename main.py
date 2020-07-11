import telebot
import validators

from config import BOT_TOKEN, NAME_OF_FILE
from script import make_screen

client = telebot.TeleBot(BOT_TOKEN)

@client.message_handler(commands=['start'])
def welcome(message):
    client.send_message(
        chat_id=message.chat.id,
        text='*Привет!* Скрины надо? 😏\n\nВведи *URL*, по которому нужно сделать скрин (не забудь добавить "http://"):',
        parse_mode='Markdown'
        )

@client.message_handler(content_types=['text'])
def url_handler(message):
    valid=validators.url(message.text)
    if valid==True:
        make_screen(message.text)
        photo = open(NAME_OF_FILE, 'rb')
        client.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption="Всё получилось 🥳"
            )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text='Хммм... Что-то пошло не так ☹️\n\nПроверь, пожалуйста, ссылку 🙏🏻'
            )


if __name__ == '__main__':
    client.polling(none_stop=True)