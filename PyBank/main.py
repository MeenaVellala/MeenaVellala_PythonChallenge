# Script to create a file path and read csv file
import os
import csv
csvpath = os.path.join('PyBank\Resources', 'budget_data.csv')
change = []
profitnloss = []
month = []
# with open(the path) as csvfile:
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents 
    csvreader = csv.reader(csvfile, delimiter=',')
    # Header row 
    csv_header = next(csvreader)
# The number of rows in the csv file is the total months
    for csvrow in csvreader:
                # months and profitsnloss are added as column to a list 
        month.append(csvrow[0])
        profitnloss.append(int(csvrow[1]))
# calculating the change, save it in a variable and the change is the difference between next months value and the current month
    for i in range (len(profitnloss)-1):
        change.append(profitnloss[i+1]-profitnloss[i])

#The greatest increase and decrease in values are captured using max, min and their corresponding months are calculated using
greatest_increase_value = max(change)
greatest_date = change.index(greatest_increase_value)
greatest_decrease_value = min(change)
loss_date = change.index(greatest_decrease_value)
# Print the final analysis
print('Financial Analysis')
print('-------------------------')
print(f'Total Months: {len(month)} ')
print(f"Total: ${sum(profitnloss)}")
print(f"Average Change: ${round(sum(change)/len(change),2)}")
print(f"Greatest Increase in Profits: {month[greatest_date + 1]} (${str(greatest_increase_value)})")
print(f"Greatest Decrease in Profits: {month[loss_date + 1]} (${str(greatest_decrease_value)})")
#Write to text file
output_path = "budget_analysis.txt"

file =  open(output_path, 'w') 
file.write("Financial Analysis\n")
file.write("----------------------------\n")
file.write(f"Total Months: {len(month)}\n")
file.write(f"Total: ${sum(profitnloss)} \n")
file.write(f"Average Change: ${round(sum(change)/len(change),2)}\n")
file.write(f"Greatest Increase in Profits: {month[greatest_date + 1]} (${str(greatest_increase_value)}) \n")
file.write(f"Dreatest Decrease in Profits: {month[loss_date + 1]} (${str(greatest_decrease_value)})\n")
file.close()












  
