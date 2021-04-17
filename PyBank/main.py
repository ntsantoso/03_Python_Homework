    #Import the necessary tools to start the code
import os
import csv
  
    #Create a filepath to reference the data source
filepath = os.path.join("Resources","budget_data.csv")
  
    #Set up empty lists for storing values
months = []
net_change = []

    #Set counters to 0 to begin counting
net_profit = 0
months_count = 0
    #Declaring previous_value as a variable to store the change in Profit/Losses in the for loop
previous_value = 0

    #Open the file with csvreader before coding in formulas to obtain results
with open(filepath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip the header to prevent any invalid str and int operations
    header = next(csvreader)

    #Loop through the data 
    for row in csvreader:

    #Store the months string into empty months list
        months.append(str(row[0]))

    #The total number of months included in the dataset
        months_count += 1

    #The net total amount of "Profit/Losses" over the entire period
        net_profit += int(row[1])

    #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        net_change.append(int(row[1]) - previous_value)
        previous_value = int(row[1])

    #The greatest increase in profits (date and amount) over the entire period
        #Call out using the max function in our net_change list
        max_increase = max(net_change)

        #Call out the month associated with the max_increase, consulted with Ronald to find the command using index.
        max_increase_month = months[net_change.index(max_increase)]

    #The greatest decrease in losses (date and amount) over the entire period
        #Call out using the min function in our net_change list
        max_decrease = min(net_change)

        #Call out the month associated with the max_increase
        max_decrease_month = months[net_change.index(max_decrease)]

#Delete first value in the list to discard the first net_change value
del net_change[0]

#Divide net_change by total months-1 because the number of changes is one less than total count of months
avg_change = sum(net_change)/(months_count-1)

#Print out results
print(f'''
    Financial Analysis
    =====================
    Total Months: {months_count}
    Total: ${net_profit}
    Average Change: {avg_change}
    Greatest Increase in Profits: {max_increase_month} (${max_increase})
    Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})
''')

    #Put output into txt file
final_results = "final_results.txt"
with open(final_results,"w") as results:
    results.write(f'''
    Financial Analysis
    =====================
    Total Months: {months_count}
    Total: ${net_profit}
    Average Change: {avg_change}
    Greatest Increase in Profits: {max_increase_month} (${max_increase})
    Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})
''')