from subprocess import PIPE
from subprocess import Popen
import config
import telebot

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['time'])
def date_time(message):
    process = Popen("date", stdout=PIPE)
    text, error = process.communicate()
    
    if error:
        text = "You have an error"
    else:
        text = text.decode("utf-8")

    bot.send_message(
        chat_id=message.chat.id,
        text=text
    )


@bot.message_handler()
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
