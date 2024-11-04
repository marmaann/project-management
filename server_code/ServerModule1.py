import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

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
