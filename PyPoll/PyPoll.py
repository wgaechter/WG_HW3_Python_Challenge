import os
import csv

election_csv = os.path.join('Resources', 'election_data.csv')

with open(election_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    
    header = next(csvreader)

    print(header)
