from ._anvil_designer import ViewRecallsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ViewRecalls(ViewRecallsTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Populate the dropdown with Recall IDs from the server
        self.drop_down_1.items = anvil.server.call('get_high_priority_recalls')

    def drop_down_1_change(self, **event_args):
        """This method is called when an item is selected"""
        selected_record = self.drop_down_1.selected_value
        if selected_record:
            # Display additional information from the selected record
            self.label_priority_level.text = f"Priority Level: {selected_record['recall priority']}"
            self.label_description.text = f"Description: {selected_record['recall']}"
