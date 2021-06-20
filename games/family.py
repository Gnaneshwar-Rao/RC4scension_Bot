import constants
import interface
from games.game import Game

class Family(interface.implements(Game)):
  def __init__(self, bot):
    self.bot = bot
    self.name = constants.GAME_FAMILY

  def get_bot(self):
    return self.bot

  def get_name(self):
    return self.name

  def get_prompt(self):
    return "Starting " + self.name + "! \nThe Aim of this Game is to to communicate with their OG to pass them ingredients that they need but do not have. Ingredients are passed to other players by swiping them across the screen either left or right!\nA rough guide to set up the game and the game objectives can be found in the link given below:\nLink : https://docs.google.com/presentation/d/1VWGYm8WvgsvbPmdnaqwr-ZF_-gtv069344pbYBgw8y4/edit?usp=sharing \n\nThe Game can be through the Family Style app and it should be run on Kumospace with 2 groups arranged in a circle!"
  
  def get_success_code_1(self):
    return 'DELPHIC'
  
  def get_success_code_2(self):
    return 'DELPHIC'
  
  def get_game_success_text(self):
    return 'Congratulations! You have passed this round. Enter "DELPHIC" in the survey link given below: \n\nLink : https://forms.gle/U1DvoKiErTguQBpZ9 \n\nPlease press the button and choose the next game :)'
