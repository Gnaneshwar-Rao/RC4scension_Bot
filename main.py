import constants
import os
import telebot
from telebot import types
from games.haxball import Haxball
from games.uno import Uno
from games.skribbl import Skribbl
from games.gartic import Gartic
from games.codenames import Codenames
from games.spyfall import Spyfall
from games.family import Family
from games.scatter import Scatter
from games.secret import Secret
from games.agar import Agar
from games.hide import Hide
from games.smashkarts import Smashkarts
from games.jeopardy import Jeopardy
from games.welp import Welp
from flask import Flask, request

PORT = int(os.environ.get('PORT', 5000))
bot = telebot.TeleBot(constants.API_KEY)
server = Flask(__name__)


def send_message(chat_id, message, markup = None):
  bot.send_message(chat_id, message, reply_markup = markup)

def handle_game_start(message):
  game = message.text
  gameObject = None
  
  if game == constants.GAME_HAXBALL:
    gameObject = Haxball(bot)
  elif game == constants.GAME_UNO:
    gameObject = Uno(bot)
  elif game == constants.GAME_SKRIBBL:
    gameObject = Skribbl(bot)
  elif game == constants.GAME_GARTIC:
    gameObject = Gartic(bot)
  elif game == constants.GAME_CODENAMES:
    gameObject = Codenames(bot)
  elif game == constants.GAME_SPYFALL:
    gameObject = Spyfall(bot)
  elif game == constants.GAME_FAMILY:
    gameObject = Family(bot)
  elif game == constants.GAME_SCATTER:
    gameObject = Scatter(bot)
  elif game == constants.GAME_SECRET:
    gameObject = Secret(bot)
  elif game == constants.GAME_AGAR:
    gameObject = Agar(bot)
  elif game == constants.GAME_HIDE:
    gameObject = Hide(bot)
  elif game == constants.GAME_SMASHKARTS:
    gameObject = Smashkarts(bot)
  elif game == constants.GAME_JEOPARDY:
    gameObject = Jeopardy(bot)
  # elif game == constants.GAME_WELP:
  #   gameObject = Welp(bot)
  else:
    print(game)
    return
  
  gameObject.send_prompt(message)
  

@bot.message_handler(commands=['start'])
def start(message):
  markup1 = types.ReplyKeyboardMarkup(row_width=1)
  welcomeOption = types.KeyboardButton(constants.LETS_PLAY_GAME)
  markup1.add(welcomeOption)
  send_message(message.chat.id, constants.WELCOME_MESSAGE, markup1)

def get_games_list_markup():
  markup = types.ReplyKeyboardMarkup(row_width=4)
  gamesList = constants.get_game_names()
  for game in gamesList:
    markup.add(types.KeyboardButton(game))
  return markup 

@bot.message_handler(commands=['listGames'])
def list_games(message):
  markup = get_games_list_markup()
  message = bot.reply_to(message, "Welcome to the RACE against TIME, where your sole objective is to find the misfits among your Clan members before it's too late. \nIn order to beat the sabotagers, Choose one of 15 games to start finding the misfits!", reply_markup = markup)
  handle_game_start(message)
  bot.register_next_step_handler(message, handle_game_start)

def send_error_msg(chat_id):
  send_message(chat_id, 'Sorry, I could not understand your message :(')

@bot.edited_channel_post_handler(content_types=['text'])
@bot.message_handler(content_types=['text'])
def initialHandler(message):
  text = message.text
  chat_id = message.chat.id
  if (text == constants.LETS_PLAY_GAME or text == constants.LIST_ALL_GAMES):
    list_games(message)
  else:
    send_error_msg(chat_id)

@server.route('/' + constants.API_KEY, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@server.route("/")
def webhook():
  bot.remove_webhook()
  bot.set_webhook('https://secret-harbor-40487.herokuapp.com/' + constants.API_KEY) 
  return "!", 200
  # bot.polling(none_stop=False, interval=0, timeout=20)

if __name__ == "__main__":
  server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
