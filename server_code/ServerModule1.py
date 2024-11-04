import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_high_priority_recalls():
    recalls = app_tables.high_priority_recalls.search()
    return [
        {
            "id": recall["Recall ID"],
            "priority": recall["Recall Priority"],
            "description": recall["Recall"]
        }
        for recall in recalls
    ]
@anvil.server.callable
def get_high_priority_products():
    # Filter for records where "Recall Priority" is "High"
    high_priority_recalls = app_tables.high_priority_recalls.search(
        **{"Recall Priority": "High"}  # Use ** to handle spaces in column names
    )

    # Return data in a format suitable for displaying in the Data Grid
    return [
        {
            "id": recall["Recall ID"],
            "priority": recall["Recall Priority"],
            "description": recall["Recall"]
        }
        for recall in high_priority_recalls
    ]

