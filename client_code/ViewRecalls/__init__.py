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
        self.drop_down_1.items = [(str(recall["id"]), recall) for recall in anvil.server.call('get_high_priority_recalls')]

    def drop_down_1_change(self, **event_args):
        """This method is called when an item is selected"""
        selected_record = self.drop_down_1.selected_value  # This should be the full record
        if selected_record:
            # Update labels with details
            self.label_priority_level.text = f"Priority Level: {selected_record['priority']}"
            self.label_description.text = f"Description: {selected_record['description']}"
