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