import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    #month_list = (list(csvreader))
    #total_months = len(month_list)
    row_total = 0
    total = 0
    for row in csvreader:
        row_total += 1
        total = total + int(row[1])

    



    print(f"Total Months: {row_total}")
    print(f"Total Profit: ${total}")
    #print(f"Average Profit: {mean_profit}")
    #print(f"High Profit: ${max_profit}")
    #print(f"Low Profit: {min_profit}")