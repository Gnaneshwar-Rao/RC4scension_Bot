import constants
import interface
from games.game import Game

class Skribbl(interface.implements(Game)):
  def __init__(self, bot):
    self.bot = bot
    self.name = constants.GAME_SKRIBBL

  def get_bot(self):
    return self.bot

  def get_name(self):
    return self.name

  def get_prompt(self):
    return "Starting " + self.name + "! \nThe Aim of this Game is to attain the highest point which can be accumulated should the player either guess the drawer's drawing correctly or if they succeed in making people guess the word of the drawing!\nA rough guide to set up the game and the game objectives can be found in the link given below:\nLink : https://docs.google.com/presentation/d/1rwxu0EDlkaIBZAZMJ3wDRzIfiuxKt8qiPSNVruFeTBM/edit?usp=sharing \n\nThe Game link is as follows: https://skribbl.io/ and it should be run on Zoom"
  
  def get_success_code_1(self):
    return 'BANSHEE'
  
  def get_success_code_2(self):
    return 'BANSHEE'
  
  def get_game_success_text(self):
    return 'Congratulations! You have passed this round. Enter "BANSHEE" in the survey link given below: \n\nLink : https://forms.gle/U1DvoKiErTguQBpZ9 \n\nPlease press the button and choose the next game :)'
