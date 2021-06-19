import constants
import interface
from games.game import Game

class Hide(interface.implements(Game)):
  def __init__(self, bot):
    self.bot = bot
    self.name = constants.GAME_HIDE

  def get_bot(self):
    return self.bot

  def get_name(self):
    return self.name 

  def get_prompt(self):
    return "Starting " + self.name + "! \nThe Aim of this Game is for the hunters to find the props and shoot/throw grenades at them while the props have to avoid getting shoy by the hunters! So CHOOSE your props wisely..\nA rough guide to set up the game and the game objectives can be found in the link given below:\nLink : https://docs.google.com/presentation/d/1MgQN0la2sZO5s5uRmAOh5JxLOLsfibHNNEpMoHucpXI/edit?usp=sharing"
  
  def get_success_code_1(self):
    return 'PROTEAN'
  
  def get_success_code_2(self):
    return 'PROTEAN'
  
  def get_game_success_text(self):
    return 'Congratulations! You have passed this round. Enter "PROTEAN" in the survey link given below: \n\nLink : https://forms.gle/U1DvoKiErTguQBpZ9 \n\nPlease press the button and choose the next game :)'
