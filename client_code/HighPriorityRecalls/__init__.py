from ._anvil_designer import HighPriorityRecallsTemplate
from anvil import *
import anvil.server

class HighPriorityRecalls(HighPriorityRecallsTemplate):
    def __init__(self, **properties):
        # Initialize form components
        self.init_components(**properties)
        
        # Fetch data from the server and assign it to the Data Grid
        try:
            high_priority_data = anvil.server.call('get_high_priority_products')
            print(f"Fetched data: {high_priority_data}")  # Debug statement
            self.data_grid_1.items = high_priority_data  # Populate the Data Grid
            print(f"Data Grid items: {self.data_grid_1.items}")  # Debug statement
        except anvil.server.AnvilError as e:
            alert(f"An error occurred: {str(e)}", title="Error", large=True)

    def button_1_click(self, **event_args):
        """Delete the selected recall when button is clicked."""
        selected_item = self.data_grid_1.selected_row  # Get the selected row from Data Grid
        
        if selected_item:
            # Confirm deletion with the user
            confirm_delete = confirm(f"Are you sure you want to delete the recall '{selected_item['Recall']}'?")
            
            if confirm_delete:
                # Call the server function to delete the recall by its ID
                anvil.server.call('delete_recall', selected_item['Recall ID'])
                
                # Refresh the Data Grid to reflect deletion
                self.refresh_data_grid()
        else:
            alert("Please select a recall to delete.", title="No Selection")
