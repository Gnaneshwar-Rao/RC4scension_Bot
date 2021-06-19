import constants
import telebot
from telebot import types
from games.haxball import Haxball
from games.uno import Uno
import os


bot = telebot.TeleBot(constants.API_KEY)


def send_message(chat_id, message, markup = None):
  bot.send_message(chat_id, message, reply_markup = markup)

def handle_game_start(message):
  game = message.text
  gameObject = None
  
  if game == constants.GAME_HAXBALL:
    gameObject = Haxball(bot)
  elif game == constants.GAME_UNO:
    gameObject = Uno(bot)
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
  message = bot.reply_to(message, "Choose one of 15 games to start finding the misfits!", reply_markup = markup)
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

def main():
  bot.polling(none_stop=False, interval=0, timeout=20)
  # bot.set_webhook(url='https://fast-bayou-59025.herokuapp.com/')
  bot.delete_webhook()
  # bot.start_

if __name__ == "__main__":
  main()
