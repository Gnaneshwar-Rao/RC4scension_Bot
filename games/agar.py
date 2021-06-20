import constants
import interface
from games.game import Game

class Agar(interface.implements(Game)):
  def __init__(self, bot):
    self.bot = bot
    self.name = constants.GAME_AGAR

  def get_bot(self):
    return self.bot

  def get_name(self):
    return self.name

  def get_prompt(self):
    return "Starting " + self.name + "! \nThe Aim of this Game is to control your tiny cell and eat other smaller cells to grow bigger, while at the same time avoiding getting eaten by bigger cells.\nA rough guide to set up the game and the game objectives can be found in the link given below:\nLink : https://docs.google.com/presentation/d/1nqpS5bXdMIyVhUYPq-uPnUdxq76JToKCSgz56omi9YQ/edit?usp=sharing \n\nThe Game can be through https://pinka.herokuapp.com/ and it should be run on Zoom in party mode!"
  
  def get_success_code_1(self):
    return 'ODYSSEY'
  
  def get_success_code_2(self):
    return 'ODYSSEY'
  
  def get_game_success_text(self):
    return 'Congratulations! You have passed this round. Enter "ODYSSEY" in the survey link given below: \n\nLink : https://forms.gle/U1DvoKiErTguQBpZ9 \n\nPlease press the button and choose the next game :)'
