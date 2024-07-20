# Script to create a file path and read csv file
import os
import csv
csvpath = os.path.join('PyPoll','Resources', 'election_data.csv')
votes = []
charles_casper_stockham = 0
diana_degette = 0
raymon_anthony_doane = 0
# with open(the path) as csvfile:
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents 
    csvreader = csv.reader(csvfile, delimiter=',')
    # Header row 
    csv_header = next(csvreader)
# The number of rows in the csv file is the total months
    for csvrow in csvreader:
                # ballot id is unique value and we are appending this column to the votes list 
        votes.append(csvrow[0])
        # counting the number of votes each candidate has received by counting the number of occurences each contestant name has come in the candidate column
        if csvrow[2] == "Charles Casper Stockham":
            charles_casper_stockham = charles_casper_stockham + 1
        elif csvrow[2] == "Diana DeGette":
            diana_degette = diana_degette + 1
        elif csvrow[2] == "Raymon Anthony Doane":
            raymon_anthony_doane = raymon_anthony_doane + 1
# calculation for the % of vote against each candidate
    contestant_1 = round(((charles_casper_stockham)/len(votes))*100,3)
    contestant_2 = round(((diana_degette)/len(votes))*100,3)
    contestant_3 = round(((raymon_anthony_doane)/len(votes))*100,3)
# create a dictionary to save the values 
    dic_votes = {"Charles Casper Stockham": charles_casper_stockham, "Diana DeGette": diana_degette, "Raymon Anthony Doane": raymon_anthony_doane }
    winner = max(dic_votes,key=dic_votes.get)

#print the results
print("Election Results")
print("----------------------------")
print(f"Total Votes: {len(votes)}")
print("----------------------------")
print(f"Charles Casper Stockham: {contestant_1}% ({charles_casper_stockham})")
print(f"Diana DeGette: {contestant_2}% ({diana_degette})")
print(f"Raymon Anthony Doane: {contestant_3}% ({raymon_anthony_doane})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

#Write to text file
output_path = "election_result.txt"

file =  open(output_path, 'w') 


file.write("Election Results\n")
file.write("----------------------------\n")
file.write(f"Total Votes: {len(votes)}\n")
file.write("----------------------------\n")
file.write(f"Charles Casper Stockham: {contestant_1}% ({charles_casper_stockham})\n")
file.write(f"Diana DeGette: {contestant_2}% ({diana_degette})\n")
file.write(f"Raymon Anthony Doane: {contestant_3}% ({raymon_anthony_doane}) \n")
file.write("----------------------------\n")
file.write(f"Winner: {winner}\n")
file.write("----------------------------\n")

file.close()


    
        



        