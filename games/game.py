import constants
import interface
from telebot import types

class Game(interface.Interface):
  def get_prompt(self):
    pass
  
  def get_bot(self):
    pass
  
  def get_success_code_1(self):
    pass

  def get_success_code_2(self):
    pass
  
  def get_game_success_text(self):
      pass

  @interface.default
  def send_prompt(self, message):
    """Sends game prompt to the user"""
    prompt = self.get_prompt()
    bot = self.get_bot()
    try:
        message = bot.reply_to(message, prompt)
        message = bot.reply_to(message, "Please enter Code 1")
        bot.register_next_step_handler(message, self.process_code_1)
    except Exception as e:
        bot.reply_to(message, 'oooops')

  @interface.default
  def process_code_1(self, message):
      """Process the first code given by the user"""
      bot = self.get_bot()
      success_code_1 = self.get_success_code_1()
      try:
        code = message.text
        if code == success_code_1:
          message = bot.reply_to(message, "Congratulations!")
          message = bot.reply_to(message, "Please enter Code 2")
          bot.register_next_step_handler(message, self.process_code_2)
        else:
          message = bot.reply_to(message, "That does not seem right :(")
          message = bot.reply_to(message, "Please enter Code 1")
          bot.register_next_step_handler(message, self.process_code_1)
      except Exception as e:
          bot.reply_to(message, 'oooops')
     
  @interface.default
  def process_code_2(self, message):
    """Process the second code given by the user"""
    bot = self.get_bot()
    success_code_2 = self.get_success_code_2()
    game_success_text = self.get_game_success_text()
    try:
      code = message.text
      if code == success_code_2:
        markup = types.ReplyKeyboardMarkup(row_width=4)
        backButton = types.KeyboardButton(constants.LIST_ALL_GAMES)
        markup.add(backButton)
        message = bot.reply_to(message, game_success_text, reply_markup=markup)
      else:
        message = bot.reply_to(message, "That does not seem right :(")
        message = bot.reply_to(message, "Please enter Code 2")
        bot.register_next_step_handler(message, self.process_code_2)
    except Exception as e:
      bot.reply_to(message, 'oooops')  