# Import Modules 
import csv

# Path to file to import for Python Bank Homework from "Resources" Folder
raw_csv_data = "resources/budget_data.csv"

# Read in the CSV File
with open(raw_csv_data) as csvfile:
    bank_data = csv.reader(csvfile)

# Skip initial header (string) in file
    next(bank_data)

# Create lists for variables (Date, Profit/Losses)
    date = []
    profitloss = []
    change_in_profitloss = []
   
# For Loop equaling Total Date and Profit/Losses using append 
    for row in bank_data:
        date.append(row[0])
        profitloss.append(float(row[1]))

# Print Total Profit/Loss and Total Months   
    print("Financial Analysis")
    print("------------------------")  
    print("Total Profit/Loss $",sum(profitloss))
    print("Total Months",len(date))

# For Loop equaling average, min, max Total Profit/Loss 
for i in range(1,len(profitloss)):
    change_in_profitloss.append(profitloss[i] - profitloss[i-1])
    average_change_in_profitloss = sum(change_in_profitloss)/len(change_in_profitloss)
    maximum_profitloss = max(change_in_profitloss)
    minimum_profitloss = min(change_in_profitloss)
    max_profitloss_date = str(date[change_in_profitloss.index(max(change_in_profitloss))])
    min_profitloss_date = str(date[change_in_profitloss.index(min(change_in_profitloss))])
print(max_profitloss_date)
# Print Average, Minimum, Maximum Total Profit/Loss
print("Average Change Profit/Loss $", round(average_change_in_profitloss))
print("Largest Increase in Revenue:", max_profitloss_date,"($", maximum_profitloss,")")
print("Largest Decrease in Revenue:", min_profitloss_date,"($", minimum_profitloss,")")

# F-String to print text file of results
maxim = (f"{max_profitloss_date} {maximum_profitloss}")
minim = (f"{min_profitloss_date} {minimum_profitloss}")
budget=(f"Financial Analysis \n ---------------- \nTotal Months: {len(date)}\nTotal: {sum(profitloss)}\nAverage Change Profit/Loss: {round(sum(change_in_profitloss)/len(change_in_profitloss))}\nLargest Increase in Revenue: {maxim} \nLargest Decrease in Revenue: {minim}")

print(budget)

budget_results = open("budget_results.txt", "w")
budget_results.write(budget)
budget_results.close()












  