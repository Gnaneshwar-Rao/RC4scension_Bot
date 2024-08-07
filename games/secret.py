import constants
import interface
from games.game import Game

class Secret(interface.implements(Game)):
  def __init__(self, bot):
    self.bot = bot
    self.name = constants.GAME_SECRET 

  def get_bot(self):
    return self.bot

  def get_name(self):
    return self.name

  def get_prompt(self):
    return "Starting " + self.name + "! \nThe Aim of this Game is to assume the roles of liberals and fascists in the Reichstag of the Weimar Republic, with one player becoming Hitler. To win the game, both parties are set to competitively enact liberal and fascist policies, respectively, or complete a secondary objective directly involving Hitler.\nA rough guide to set up the game and the game objectives can be found in the link given below:\nLink : https://docs.google.com/presentation/d/1qOwFONVxZtMbqtj7FD-Kd-S352P2BgcN4vhvajaXFh4/edit?usp=sharing \n\nThe Game link is as follows: https://secret-hitler.com/ and it should be run on Zoom"
  
  def get_success_code_1(self):
    return 'NEREID'
  
  def get_success_code_2(self):
    return 'NEREID'
  
  def get_game_success_text(self):
    return 'Congratulations! You have passed this round. Enter "NEREID" in the survey link given below: \n\nLink : https://forms.gle/U1DvoKiErTguQBpZ9 \n\nPlease press the button and choose the next game :)'
