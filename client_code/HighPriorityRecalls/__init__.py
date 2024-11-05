from ._anvil_designer import HighPriorityRecallsTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class HighPriorityRecalls(HighPriorityRecallsTemplate):
    def __init__(self, **properties):
        # Initialize form components
        self.init_components(**properties)
        
        # Fetch data from the server and assign it to the Repeating Panel
        try:
            high_priority_data = anvil.server.call('get_high_priority_products')
            print(f"Fetched data: {high_priority_data}")  # Debug statement
            self.repeating_panel_1.items = high_priority_data  # Populate the Repeating Panel
        except Exception as e:  # Generic exception handling
            alert(f"An error occurred: {str(e)}", title="Error", large=True)

    def button_1_click(self, **event_args):
        """Delete the selected recall when button is clicked."""
        selected_item = self.repeating_panel_1.get_components()[0].item if self.repeating_panel_1.get_components() else None
        
        if selected_item:
            # Confirm deletion with the user
            confirm_delete = confirm(f"Are you sure you want to delete the recall '{selected_item['Recall']}'?")
            
            if confirm_delete:
                # Call the server function to delete the recall by its ID
                anvil.server.call('delete_recall', selected_item['Recall ID'])
                
                # Refresh the Repeating Panel to reflect deletion
                self.refresh_data_grid()
        else:
            alert("Please select a recall to delete.", title="No Selection")
