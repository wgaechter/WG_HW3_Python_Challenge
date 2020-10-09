import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    #month_list = (list(csvreader))
    #total_months = len(month_list)

    for row in csvreader:
        month_list = list(row[0])
        total_months = len()

    total = 0
    for row in csvreader:
        total = total + int(row[1])

    



    #print(f"Total Months: {total_months}")
    print(f"Total Profit: ${total}")
    #print(f"Average Profit: {mean_profit}")
    #print(f"High Profit: ${max_profit}")
    #print(f"Low Profit: {min_profit}")