import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    month = []
    profit = []
    x_list = []

    for row in csvreader:
        month.append(row[0])
        profit.append(float(row[1]))

    row_total = len(month)
    total = sum(profit)

    #Big shoutout to Rama for the help with this!
    for i in range(1, len(profit)):
        x_list.append(profit[i] - profit[i-1])

    x_avg = sum(x_list) / len(x_list)

    max_profit = max(x_list)
    min_profit = min(x_list)

    max_date = str(month[x_list.index(max(x_list)) + 1])
    min_date = str(month[x_list.index(min(x_list)) + 1])

    print("")
    print("Financial Analysis")
    print("-----------------------------------")
    print(f"Total Months: {row_total}")
    print(f"Total Profit: ${total}")
    print(f"Average Profit: ${x_avg}")
    print(f"High Profit: {max_date} (${max_profit})")
    print(f"Low Profit: {min_date} (${min_profit})")