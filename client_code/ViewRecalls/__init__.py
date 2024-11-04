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
        
        # Get recalls from server
        recalls = anvil.server.call('get_high_priority_recalls')
        
        # Format the items for the dropdown - each item will be a tuple of (display_text, record)
        formatted_items = [(f"Recall #{i+1}", recall) for i, recall in enumerate(recalls)]
        
        # Set the dropdown items
        self.drop_down_1.items = formatted_items
        
    def drop_down_1_change(self, **event_args):
        """This method is called when an item is selected"""
        selected_record = self.drop_down_1.selected_value
        if selected_record:
            # Display additional information from the selected record
            self.label_priority_level.text = f"Priority Level: {selected_record['Recall Priority']}"
            self.label_description.text = f"Description: {selected_record['Recall']}"
            self.label_id.text = f"Recall ID: {selected_record['Recall ID']}"  # if you have a label for the ID
