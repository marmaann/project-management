from ._anvil_designer import HighPriorityRecallsTemplate
from anvil import *
import anvil.server

class HighPriorityRecalls(HighPriorityRecallsTemplate):
    def __init__(self, **properties):
        # Initialize form components
        self.init_components(**properties)
        
        # Fetch data from the server when the form loads
        try:
            high_priority_data = anvil.server.call('get_high_priority_products')
            # Bind the fetched data to the Data Grid's items property
            self.data_grid_1.items = high_priority_data
        except anvil.server.AnvilError as e:
            alert(f"An error occurred: {str(e)}", title="Error", large=True)