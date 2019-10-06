from subprocess import PIPE
from subprocess import Popen
import config
import telebot
import os, time

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


@bot.message_handler(commands=['music'])
def send_music(message):
    for file in os.listdir("music/"):
        if file.split(".")[-1] == "ogg":
            f = open("music/" + file, "rb")
            msg = bot.send_voice(message.chat.id, f, None)
            bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id=msg.message_id)
        time.sleep(3)


if __name__ == '__main__':
    bot.polling(none_stop=True)
