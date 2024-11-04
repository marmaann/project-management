import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_high_priority_recalls():
    # Fetch all records with "Recall Priority" set to "High"
    high_priority_recalls = app_tables.high_priority_recalls.search()
    
    # Format the records into a list of dictionaries for the client
    return [
        {
            "Recall ID": recall["Recall ID"],
            "Recall Priority": recall["Recall Priority"],
            "Recall": recall["Recall"]
        }
        for recall in high_priority_recalls
    ]
@anvil.server.callable
def get_high_priority_products():
    # Fetch records where "Recall Priority" is "High"
    high_priority_recalls = app_tables.high_priority_recalls.search(
        **{"Recall Priority": "High"}
    )

    # Log data for debugging
    records = [
        {
            "Recall ID": recall["Recall ID"],
            "Recall Priority": recall["Recall Priority"],
            "Recall": recall["Recall"]
        }
        for recall in high_priority_recalls
    ]
    print("Fetched records:", records)  # This will log the data to server logs

    # Return data
    return records
@anvil.server.callable
def delete_recall(recall_id):
    # Find the recall record by its Recall ID
    record = app_tables.high_priority_recalls.get(Recall_ID=recall_id)
    if record:
        record.delete()
def refresh_data_grid(self):
    """Refresh the data in the Data Grid."""
    high_priority_data = anvil.server.call('get_high_priority_products')
    self.data_grid_1.items = high_priority_data  # Refresh Data Grid items

