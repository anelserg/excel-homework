# First we'll import the os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'budget_data.csv')

#Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    budgetCsvReader = csv.reader(csvfile, delimiter=',')

    print(budgetCsvReader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(budgetCsvReader)
    print(f"CSV Header: {csv_header}")

    # setting variables to 0
    monthsTotal = 0
    netTotalProfitLosses = 0
    previousRowValue = 0
    currentRowValue = 0
    changeTotal = 0
    changeCount = 0
    maxProfitChange = -1000000
    minProfitChange = 1000000
    
    # starting and empty list to add to it later the change in profit between every month
    #changeList = []
    
    # starting a for loop to read in the csv file
    for row in budgetCsvReader:
        #total number of months in the dataset
        monthsTotal = monthsTotal + 1
        #creating the variables for current row and previous row to make the 
        # difference between them
        currentRowValue = int(row[1])
        # the difference btween the months
        netTotalProfitLosses = netTotalProfitLosses + currentRowValue

        # starting an if condition to exclude the very first row being subtracted because otherwise it'll
        # throwing an error when we come to subtract the current row from it
        if previousRowValue != 0:
            change = currentRowValue - previousRowValue
            changeTotal = changeTotal + change
            changeCount = changeCount + 1

            # Max profits
            if change > maxProfitChange:
                maxProfitChange = change
                maxDate = row[0]

            # Min profits
            if change < minProfitChange:
                minProfitChange = change 
                minDate = row[0]
        
        # so that it starts the loop all over again
        previousRowValue = currentRowValue

    # calculating the average change in profits and losses
    averageChange = changeTotal /changeCount
    
    

    # printing out the output    
    print("Financial Analysis")
    print("                       ")
    print("-----------------------------")
    print("                       ")
    print("Total Months: " + str(monthsTotal))
    print("Total: " + str(netTotalProfitLosses))
    print("Average Change: " + str(averageChange))
    print("Greatest Increase In Profits: " + maxDate + " ($" + str(maxProfitChange) + ")")
    print("Greatest Decrease In Profits: " + minDate + " ($" + str(minProfitChange)+ ")")
    
### starting the code to write to a csv file
# Specify the file to write to
output_path = os.path.join(".", "BudgetWriter.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvWfile:

    # Initialize csv.writer
    budgetCsvWriter = csv.writer(csvWfile, delimiter=',')

    # Write the first row (column headers)
    budgetCsvWriter.writerow(['Financial Analysis'])

    # Write the second row
    budgetCsvWriter.writerow(['                    '])

    # Write the third row
    budgetCsvWriter.writerow(['-----------------------------'])

    # Write the fourth row
    budgetCsvWriter.writerow(['                    '])

    # Write the fifth row
    budgetCsvWriter.writerow(["Total Months: " + str(monthsTotal)])

    # Write the sixth row
    budgetCsvWriter.writerow(["Total: " + str(netTotalProfitLosses)])

    # Write the seventh row
    budgetCsvWriter.writerow(["Average Change: " + str(averageChange)])

    # Write the eightth row
    budgetCsvWriter.writerow(["Greatest Increase In Profits: " + maxDate + " ($" + str(maxProfitChange) + ")"])

    # Write the ninth row
    budgetCsvWriter.writerow(["Greatest Decrease In Profits: " + minDate + " ($" + str(minProfitChange)+ ")"])