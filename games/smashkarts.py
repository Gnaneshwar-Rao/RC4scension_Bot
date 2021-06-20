import constants
import interface
from games.game import Game

class Smashkarts(interface.implements(Game)):
  def __init__(self, bot):
    self.bot = bot
    self.name = constants.GAME_SMASHKARTS

  def get_bot(self):
    return self.bot

  def get_name(self):
    return self.name

  def get_prompt(self):
    return "Starting " + self.name + "! \nThe Aim of this Game is to protect the King/Queen of your sub-OG, while attacking the King/Queen of opposing sub-OG through KARTS!\nA rough guide to set up the game and the game objectives can be found in the link given below:\nLink : https://docs.google.com/presentation/d/1Bnh7lj1THMsMrcqX03cMETITf5lt7MiKM1EkqgKPkJM/edit?usp=sharing \n\nThe Game link is as follows: https://smashkarts.io/ and it should be run on Zoom"
  
  def get_success_code_1(self):
    return 'PSYCHE'
  
  def get_success_code_2(self):
    return 'PSYCHE'
  
  def get_game_success_text(self):
    return 'Congratulations! You have passed this round. Enter "PSYCHE" in the survey link given below: \n\nLink : https://forms.gle/U1DvoKiErTguQBpZ9 \n\nPlease press the button and choose the next game :)'
