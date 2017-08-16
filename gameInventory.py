from collections import Counter
import operator
import csv

# # Comments were already written to file. Comments that start with "# #" are mine. Code was checked with PEP8.

# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification

# Displays the inventory.


def display_inventory(inventory):
    # # Creating variable that will sum up all the values.
    sum_of_inventory = 0
    print("Inventory:")
    for key, value in inventory.items():
        print(value, key)
        sum_of_inventory += value
    print("Total number of items:", sum_of_inventory, "\n")

# Adds to the inventory dictionary a list of items from added_items.


def add_to_inventory(inventory, added_items):
    inv_copy = dict(Counter(inventory) + Counter(added_items))
    # # We have to update the inventory now, otherwise later the dictionary will not show added items.
    inventory.update(inv_copy)

# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order


def print_table(inventory, order=None):
    if order == "count,desc":
        # # "inv_copy" list = 'inv' dictionary representation for sorting in desc. or asc order.
        inv_copy = sorted(inventory.items(), key=operator.itemgetter(1), reverse=True)
    elif order == "count,asc":
        inv_copy = sorted(inventory.items(), key=operator.itemgetter(1))
    else:
        print("Wrong argument\n")
        inv_copy = inventory
    # # After sorting "inv_copy" list, make it a dictionary again to be able to distinguish between keys from values.
    inv_copy = dict(inv_copy)
    sum_of_inventory = 0
    # # We distinguish longest key and value so, if one of them is longer, the other column will remain the same.
    longest_key_from_inv = len(max(inv_copy, key=len))
    longest_value_from_inv = len(str(max(inv_copy.values())))
    # # Extra space between columns for better view.
    add_space = 5
    # # One extra dash for perfect fit.
    alignment_for_dash_series = 1
    print("Inventory:")
    print("count".rjust(longest_value_from_inv + add_space), "item name".rjust(longest_key_from_inv + add_space))
    # # Printing dash series, which lenght depends on longest key and value.
    print("-" * (longest_key_from_inv + longest_value_from_inv + 2 * add_space + alignment_for_dash_series))
    for key, value in inv_copy.items():
        print(str(value).rjust(longest_value_from_inv + add_space), str(key).rjust(longest_key_from_inv + add_space))
        sum_of_inventory += value
    print("-" * (longest_key_from_inv + longest_value_from_inv + 2 * add_space + alignment_for_dash_series))
    print("Total number of items:", sum_of_inventory, "\n")

# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).


def import_inventory(inventory, filename="import_inventory.csv"):
    # # Opening csv file.
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # # Adding imported list to our dictionary.
        for row in readCSV:
            inv_copy = dict(Counter(inventory) + Counter(row))
            inventory.update(inv_copy)

# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).


def export_inventory(inventory, filename="export_inventory.csv"):
    # # Creating list to be displayed in csv file.
    list_for_import = []
    for key, value in inventory.items():
        list_for_import.extend([key] * value)
    # # Changing list to string.
    list_for_import = ",".join(list_for_import)
    # # Opening file with UTF-8 encoding for special characters.
    filename = open(filename, "w", encoding='utf-8')
    filename.write(list_for_import)
    filename.close()

# Main function sets initial variables and stores rest of the functions


def main():
    inv = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}
    display_inventory(inv)
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    add_to_inventory(inv, dragon_loot)
    display_inventory(inv)
    # # Options for 2nd argument: None, "count,desc" or "count,asc".
    print_table(inv, "count,desc")
    # # 1st argument: dictionary name, 2nd argument: csv file name.
    import_inventory(inv, "import_inventory.csv")
    print_table(inv, "count,desc")
    # # 1st argument: dictionary name, 2nd argument: csv file name.
    export_inventory(inv, "export_inventory.csv")


main()
