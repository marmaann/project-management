from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import Module1

class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def button_2_click(self, **event_args):
      userid = self.text_box_1.text
      userpw = self.text_box_2.text
      
      dtid = [r['UserID'] for r in app_tables.passwordtable.search(UserID=userid)]
      
      if userid in dtid:
        dtpw = [r['Password'] for r in app_tables.passwordtable.search()]
        if userpw in dtpw:
          Module1.userid = userid
          Module1.User_Name = [r['Name'] for r in app_tables.passwordtable.search(UserID=userid)]
          open_form('Home')
        else:
          alert('Username/password did not match')
      else:
        alert('Username/password did not match')

  # Cancel button
  def button_1_click(self, **event_args):
    self.text_box_1.text = None
    self.text_box_2.text = None
    


