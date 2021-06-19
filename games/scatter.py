import constants
import interface
from games.game import Game

class Scatter(interface.implements(Game)):
  def __init__(self, bot):
    self.bot = bot
    self.name = constants.GAME_SCATTER

  def get_bot(self):
    return self.bot

  def get_name(self):
    return self.name

  def get_prompt(self):
    return "Starting " + self.name + "! \nThe Aim of this Game is to fill in answers starting with the given letter for different categories. A point is given to players with valid answers for each category that do not clash with other player’s answers. Player with the most points wins.\nA rough guide to set up the game and the game objectives can be found in the link given below:\nLink : https://docs.google.com/presentation/d/1doAeNV2D74yex5NvrSWZ0Ge0TwTKUuGy0owRVBP8pZU/edit?usp=sharing"
  
  def get_success_code_1(self):
    return 'DIVINE'
  
  def get_success_code_2(self):
    return 'DIVINE'
  
  def get_game_success_text(self):
    return 'Congratulations! You have passed this round. Enter "DIVINE" in the survey link given below: \n\nLink : https://forms.gle/U1DvoKiErTguQBpZ9 \n\nPlease press the button and choose the next game :)'
