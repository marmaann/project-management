from ._anvil_designer import ViewRecallsTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ViewRecalls(ViewRecallsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Populate dropdown with Recall IDs from the 'High Priority Recalls' table
    records = app_tables.high_priority_recalls.search()
    self.drop_down_1.items = [(record['Recall ID'], record) for record in records]

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    selected_record = self.drop_down_1.selected_value
    if selected_record:
      # You can now work with the selected record, e.g., display more info
      alert(f"Selected Recall ID: {selected_record['Recall ID']}")