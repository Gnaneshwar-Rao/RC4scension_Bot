import constants
import interface
from games.game import Game

class Jeopardy(interface.implements(Game)):
  def __init__(self, bot):
    self.bot = bot
    self.name = constants.GAME_JEOPARDY

  def get_bot(self):
    return self.bot

  def get_name(self):
    return self.name

  def get_prompt(self):
    return "Starting " + self.name + "! \nThe Aim of this Game is to guess the questions based on the answers to questions shown and the leading Sub-OG wins by getting the higher number of correct guesses. It's time for Jeopardyyyyy!!\nA rough guide to set up the game and the game objectives can be found in the link given below:\nLink : https://drive.google.com/file/d/1oFYzwmEMPf_aKQQM1UZe9c2HUlpa-3nB/view?usp=sharing \n\nThe Game link is as follows: https://jeopardylabs.com/play/rc4-jeopardy and it should be run on Zoom"
  
  def get_success_code_1(self):
    return 'REVELRY'
  
  def get_success_code_2(self):
    return 'REVELRY'
  
  def get_game_success_text(self):
    return 'Congratulations! You have passed this round. Enter "REVELRY" in the survey link given below: \n\nLink : https://forms.gle/U1DvoKiErTguQBpZ9 \n\nPlease press the button and choose the next game :)'
