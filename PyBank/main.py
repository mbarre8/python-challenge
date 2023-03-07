
#Modules
import os
import csv

#set path for file
budget_data_path = os.path.join('Resources', 'budget_data.csv')

#open the CSV
with open(budget_data_path) as csvfile:
    budgetreader = csv.reader(csvfile,delimiter=',')

    print(budgetreader)
    csv_header = next(budgetreader)
    print(f'csv_header:{csv_header}')

    for row in budgetreader:
        print(row)


