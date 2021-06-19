import constants
import interface
from games.game import Game

class Agar(interface.implements(Game)):
  def __init__(self, bot):
    self.bot = bot
    self.name = constants.GAME_HAXBALL

  def get_bot(self):
    return self.bot

  def get_name(self):
    return self.name

  def get_prompt(self):
    return "Starting " + self.name + "! \nThe Aim of this Game is to get the ball into the opponent’s net (similar to football).\nA rough guide to set up the game and the game objectives can be found in the link given below:\nLink : https://docs.google.com/presentation/d/1nn0PBldmA-v8W55IE-4QqqKpDtX-8BJi2VJ7WnDduJI/edit?usp=sharing"
  
  def get_success_code_1(self):
    return 'ODYSSEY'
  
  def get_success_code_2(self):
    return 'ODYSSEY'
  
  def get_game_success_text(self):
    return 'Congratulations! You have passed this round. Enter "ODYSSEY" in the survey link given below: \n\nLink : https://forms.gle/U1DvoKiErTguQBpZ9 \n\nPlease press the button and choose the next game :)'
