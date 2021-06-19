import constants
import interface
from games.game import Game

class Codenames(interface.implements(Game)):
  def __init__(self, bot):
    self.bot = bot
    self.name = constants.GAME_HAXBALL

  def get_bot(self):
    return self.bot

  def get_name(self):
    return self.name

  def get_prompt(self):
    return "Starting " + self.name + "! \nThe Aim of this Game is to clear the cards laid in the grid by suggesting a single word clue that could even clear multiple cards in the grid. BUT BEWARE...if you pick the Black Card you lose the Game, so heed your Spymaster's words!!\nA rough guide to set up the game and the game objectives can be found in the link given below:\nLink : https://docs.google.com/presentation/d/190S3XEcM4aIcecwHi9lnnbwW6bXyILo4NCQHK771UGs/edit?usp=sharing"
  
  def get_success_code_1(self):
    return 'GHOUL'
  
  def get_success_code_2(self):
    return 'GHOUL'
  
  def get_game_success_text(self):
    return 'Congratulations! You have passed this round. Enter "GHOUL" in the survey link given below: \n\nLink : https://forms.gle/U1DvoKiErTguQBpZ9 \n\nPlease press the button and choose the next game :)'
