import os
import csv
import sys

election_csv = os.path.join('Resources', 'election_data.csv')

with open(election_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')

    #Vote COunt Variables
    Khan_Votes = 0
    Correy_Votes = 0
    Li_Votes = 0
    OTooley_Votes = 0
    Extra_Votes = 0

    #Vote Counter Loop
    for row in csvreader:
        candidate = str(row["Candidate"])
        if candidate == "Khan":
            Khan_Votes = (Khan_Votes + 1)
        if candidate == "Correy":
            Correy_Votes = (Correy_Votes + 1)
        if candidate == "Li":
            Li_Votes = (Li_Votes + 1)
        if candidate == "O'Tooley":
            OTooley_Votes = (OTooley_Votes + 1)


    Total_Votes = (Khan_Votes + Correy_Votes + Li_Votes + OTooley_Votes)
    

#def Election_Results()
print("")
print("Election Results")
print("--------------------------")
print(f"Total Votes: {Total_Votes}")
print("--------------------------")
print(f"Khan: {Khan_Votes}")
print(f"Correy: {Correy_Votes}")
print(f"Li: {Li_Votes}")
print(f"OTooley: {OTooley_Votes}")
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")

