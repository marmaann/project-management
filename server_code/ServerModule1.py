import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_high_priority_recalls():
    recalls = app_tables.high_priority_recalls.search()
    # Match the column names exactly
    return [
        {
            "id": recall["Recall ID"],
            "priority": recall["Recall Priority"],
            "description": recall["Recall"]
        }
        for recall in recalls
    ]

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
