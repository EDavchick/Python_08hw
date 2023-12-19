import telebot
from random import *
import json
import requests
from modul import *
# from deeppavlov import configs
# from deeppavlov.core.commands.infer import build_model
films = []

API_URL = "https://7012.deeppavlov.ai.model"
# odqa = build_model(configs.odqa.en_odqa_infer_wiki)
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=["start"])
def start_message(message):
    try:
        load()
        bot.send_message(message.chat.id, "Films")
    except:
        films.append("Matrix")
        films.append("Santa Barbara")
        films.append("Lord of Rings")
        films.append("Lion King")
        films.append("Solaris")
        bot.send_message(message.chat.id, "Films was download")

@bot.message_handler(commands=["all"])
def show_all(message):
    try:
        bot.send_message(message.chat.id, "This is your list of films")
        bot.send_message(message.chat.id, ", ".join(films))
    except:
        bot.send_message(message.chat.id, "List is empty")

@bot.message_handler(commands=["save"])
def save_all(message):
    with open("films.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(films, ensure_ascii=False))
        bot.send_message(message.chat.id, "Your films have been successfully saved in file films.json")

# @bot.message_handler(commands=["add"])
# def add_film(message):
#         bot.send_message(message.chat.id, "Your films have been successfully added in file films.json")


@bot.message_handler(commands=["wiki"])
def wiki(message):
    quest = message.text.split()[1:]
    qq = " ".join(quest)
    data = { "question_raw": [qq] }
    try:
        res = requests.post(API_URL, json=data,verify=False).json()
        bot.send_message(message.chat.id, res)
    except:
        bot.send_message(message.chat.id, "There are nothing on your request")

@bot.message_handler(content_types=["text"])
def get_text_message(message):
    if "how" in message.text.lower():
        bot.send_message(message.chat.id, "I'm fine. How are you?")

bot.polling() # старт бота, зашит цикл while true