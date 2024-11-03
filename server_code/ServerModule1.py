import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_high_priority_recalls():
    # Fetch all records with additional data
    records = app_tables.high_priority_recalls.search()
    # Return a list of tuples with Recall ID, full record
    return [(str(record['Recall ID']), record) for record in records]
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
