import constants
import interface
from games.game import Game

class Uno(interface.implements(Game)):
  def __init__(self, bot):
    self.bot = bot
    self.name = constants.GAME_UNO

  def get_bot(self):
    return self.bot

  def get_name(self):
    return self.name

  def get_prompt(self):
    return "Starting " + self.name + "! \n Hello. This is a prompt"
  
  def get_success_code_1(self):
    return '1234'
  
  def get_success_code_2(self):
    return '4567'
  
  def get_game_success_text(self):
    return 'Congratulations! You have passed this round. Please press the button and choose the next game :)'
