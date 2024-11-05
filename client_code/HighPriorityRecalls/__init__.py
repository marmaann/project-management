import anvil.tables as tables
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_high_priority_recalls():
    # Fetch all records
    high_priority_recalls = app_tables.high_priority_recalls.search()
    
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
    # Fetch only records where "Recall Priority" is "High"
    high_priority_recalls = app_tables.high_priority_recalls.search(
        Recall_Priority="High"
    )
    
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
def delete_recall(recall_id):
    # Find the recall record by its Recall ID
    record = app_tables.high_priority_recalls.get(Recall_ID=recall_id)
    if record:
        record.delete()
