from ._anvil_designer import HighPriorityRecallsTemplate
from anvil import *
import anvil.server

class HighPriorityRecalls(HighPriorityRecallsTemplate):
    def __init__(self, **properties):
        # Initialize form components and set properties
        self.init_components(**properties)
        
        # Fetch high-priority recall data from the server when the form loads
        try:
            # Call the server function to get high-priority recall data
            high_priority_data = anvil.server.call('get_high_priority_products')
            
            # Bind the fetched data to the Data Grid component's items
            self.data_grid_1.items = high_priority_data
        except anvil.server.AnvilError as e:
            # Handle potential server errors
            alert(f"An error occurred: {str(e)}", title="Error", large=True)
