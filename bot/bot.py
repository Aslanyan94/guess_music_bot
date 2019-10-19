import os
import time
import random
from SQLighter import SQLighter
from subprocess import PIPE
from subprocess import Popen
from telebot import types
import telebot
import config
import utils

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
        if file.split(".")[-1] == "mp3":
            f = open("music/" + file, "rb")
            msg = bot.send_voice(message.chat.id, f, None)
            print(file[:-4:], msg.voice.file_id)
            bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id=msg.message_id)
        time.sleep(5)



@bot.message_handler(commands=['game'])
def game(message):
    db_worker = SQLighter(config.database_name)
    row = db_worker.select_single(random.randint(1, utils.get_rows_count()))
    markup = utils.generate_markup(row[2], row[3])
    bot.send_voice(message.chat.id, row[1], reply_markup=markup)
    utils.set_user_game(message.chat.id, row[2])
    db_worker.close()


@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_answer(message):
    answer = utils.get_answer_for_user(message.chat.id)
    if not answer:
        bot.send_message(message.chat.id, 'for start game choose command /game')
    else:
        keyboard_hider = types.ReplyKeyboardRemove()
        if message.text == answer:
            bot.send_message(message.chat.id, 'Right!', reply_markup=keyboard_hider)
        else:
            bot.send_message(message.chat.id, 'Wrong answer. Try it again!', reply_markup=keyboard_hider)
        
        utils.finish_user_game(message.chat.id)



if __name__ == '__main__':
    utils.count_rows()
    random.seed()
    bot.polling(none_stop=True)
