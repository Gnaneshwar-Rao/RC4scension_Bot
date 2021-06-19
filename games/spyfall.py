import constants
import interface
from games.game import Game

class Spyfall(interface.implements(Game)):
  def __init__(self, bot):
    self.bot = bot
    self.name = constants.GAME_SPYFALL

  def get_bot(self):
    return self.bot

  def get_name(self):
    return self.name

  def get_prompt(self):
    return "Starting " + self.name + "! \nThe Aim of this Game is to find the spy hiding among the detectives.\nA rough guide to set up the game and the game objectives can be found in the link given below:\nLink : https://docs.google.com/presentation/d/1LAN95t_dBrShSVsH0LsKERBsemn2rfXMdXpXIS-icmo/edit?usp=sharing"
  
  def get_success_code_1(self):
    return 'CELESTIAL'
  
  def get_success_code_2(self):
    return 'CELESTIAL'
  
  def get_game_success_text(self):
    return 'Congratulations! You have passed this round. Enter "CELESTIAL" in the survey link given below: \n\nLink : https://forms.gle/U1DvoKiErTguQBpZ9 \n\nPlease press the button and choose the next game :)'
