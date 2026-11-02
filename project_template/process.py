"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""
import csv


def open_file():
    with open("data/disneyland_reviews.csv") as d:
        reader = csv.reader(d)
        header = next(reader)
        rows = number_of_rows(d)

    print("Data read.")
    print(f"Data has {rows} rows")

    d.close()


def number_of_rows(file):
    for i, _ in enumerate(file):
        pass
    return i + 1


