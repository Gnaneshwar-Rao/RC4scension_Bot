import constants
import interface
from games.game import Game

class Gartic(interface.implements(Game)):
  def __init__(self, bot):
    self.bot = bot
    self.name = constants.GAME_GARTIC

  def get_bot(self):
    return self.bot

  def get_name(self):
    return self.name

  def get_prompt(self):
    return "Starting " + self.name + "! \nThe Aim of this Game is to come up with a story or a catchphrase which will then be used by another person to draw a picture and another person would have to guess the phrase, and so on...\nA rough guide to set up the game and the game objectives can be found in the link given below:\nLink : https://docs.google.com/presentation/d/1OFSNY7wIuTWCKYabBNvbuzFG1rNc37dfyUDCLQnNw0E/edit?usp=sharing \n\nThe Game link is as follows: https://garticphone.com/ and it should be run on Zoom"
  
  def get_success_code_1(self):
    return 'DRYAD'
  
  def get_success_code_2(self):
    return 'DRYAD'
  
  def get_game_success_text(self):
    return 'Congratulations! You have passed this round. Enter "DRYAD" in the survey link given below: \n\nLink : https://forms.gle/U1DvoKiErTguQBpZ9 \n\nPlease press the button and choose the next game :)'

