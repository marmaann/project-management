from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import Module1
from tables import app_tables

class Home(HomeTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.label_3.text = "Welcome " + Module1.User_Name[0]

  def link_2_click(self, **event_args):
    open_form('ChangePassword')

  def link_1_click(self, **event_args):
   open_form('Logout')
    
  def link_3_click(self, **event_args):
    open_form('HighPriorityRecalls')
    pass

  def link_4_click(self, **event_args):
    open_form('ViewRecalls')
    pass



