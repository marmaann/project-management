from ._anvil_designer import ChangePasswordTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import Module1

class ChangePassword(ChangePasswordTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def button_2_click(self, **event_args):
      uid = Module1.userid
      oldpw = self.text_box_2.text
      newpw = self.text_box_3.text
      if newpw == "":
        alert('Password can not be empty')
      else:
        pw = [r['Password'] for r in app_tables.passwordtable.search(UserID=uid)]
        pw = pw[0]
        if oldpw == pw:
          row = app_tables.passwordtable.get(UserID=uid)
          row['Password'] = newpw
          alert('Password Updated Successfully')
          open_form('Login')
        else:
            alert('Incorrect Old Password')

  # Cancel button
  def button_1_click(self, **event_args):
    open_form('Home')
    


