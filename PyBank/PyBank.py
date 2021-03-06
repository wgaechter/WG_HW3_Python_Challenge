import os
import csv
import sys

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


def Analysis():
    print("")
    print("Financial Analysis")
    print("-----------------------------------")
    print(f"Total Months: {row_total}")
    print(f"Total Profit: ${total}")
    print(f"Average Change: ${x_avg}")
    print(f"Greatest Increase in Profit: {max_date} (${max_profit})")
    print(f"Greatest Decrease in Profits: {min_date} (${min_profit})")

Analysis()
#TXT OUTPUT 

output_path = os.path.join('Analysis', 'Financial_Analysis.txt')

with open(output_path, 'a') as f:
    sys.stdout = f
    Analysis()


