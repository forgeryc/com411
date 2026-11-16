"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""
import tui
import process
import visual

tui.title_screen("Disneyland Review Analyser")
process.open_file()
if tui.menu("View Data", "Visualise Data") == "a":
        tui.view_data()
else:
        tui.visualise_data()
