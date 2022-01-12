"""PyRamen Homework Starter."""

# Import libraries
import csv
from pathlib import Path

# Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('menu_data.csv')
sales_filepath = Path('sales_data.csv')

# Initialize list objects to hold our menu and sales data
menu = []
sales = []

# Read in the menu data into the menu list
with open(menu_filepath, "r") as menufile:
    menureader = csv.reader(menufile, delimiter=",")
    menu_header = next(menureader)
    for row in menureader:
        menu.append(row)

# Read in the sales data into the sales list
with open(sales_filepath, "r") as salesfile:
    salesreader = csv.reader(salesfile, delimiter=",")
    sales_header = next(salesreader)
    for row in salesreader:
        sales.append(row)

# Initialize dict object to hold our key-value pairs of items and metrics
report = {}
#'sales_item':dict.fromkeys(['count','revenue','cogs','profit'])}

# Initialize a row counter variable
row_count = 0

# Loop over every row in the sales list object

for item in sales:


    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # Initialize sales data variables
    Quantity = int(item[3])
    Menu_Item = item[4]

    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if Menu_Item not in report:
        report[Menu_Item] = {'count':0,'revenue':0,'cogs':0,'profit':0}

    # For every row in our sales data, loop over the menu records to determine a match
    for menu_item in menu: 

        # Item,Category,Description,Price,Cost
        # Initialize menu data variables
        Item = menu_item[0]
        Price = float(menu_item[3])
        Cost = int(menu_item[4])


        # Calculate profit of each item in the menu data
        Profit = Price - Cost

        # If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if Menu_Item == Item:

            # Print out matching menu data
            #print(menu_item)

            # Cumulatively add up the metrics for each item key
            report[Menu_Item]["count"] += Quantity
            report[Menu_Item]["revenue"] += Price * Quantity
            report[Menu_Item]["cogs"] += Cost * Quantity
            report[Menu_Item]["profit"] += Profit * Quantity

        # Else, the sales item does not equal any fo the item in the menu data, therefore no match
        else:
            continue
            #print(f"{Menu_Item} does not equal {Item}! NO MATCH!")


    # Increment the row counter by 1
    row_count += 1

# Print total number of records in sales data
print(len(report.keys()))

# Write out report to a text file (won't appear on the command line output)
with open("records.txt",'w') as data:
    data.write(str(report))