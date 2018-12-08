import os
import csv

# Path to collect data from the Resources folder
pybank_csv = os.path.join('.', 'Resources', 'budget_data.csv')


# Read in the CSV file
with open(pybank_csv, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    header = next(csvreader)
    month = 0
    currentprofit = 0
    totalprofit = 0
    lastprofit = 0
    change = 0
    sumchange = 0
    maxchange = 0
    maxmonth = 0
    minchange = 0
    minmonth = 0
    for row in csvreader:
        month += 1
        currentprofit = row[1]
        totalprofit = float(currentprofit) + totalprofit
        if month >1:
            change = float(currentprofit) - float(lastprofit)
            sumchange = change + sumchange
            if change > maxchange:
                maxchange = change
                maxmonth = row[0]
            if change < minchange:
                minchange = change
                minmonth = row[0]
        lastprofit = currentprofit
            
averageprofit = round(sumchange/(month-1),2)
maxchange = round(maxchange,2)
minchange = round(minchange,2)
    
#print(f"Total Months: {month}")
#print(f"Total Profits and Losses: ${totalprofit}")
#print(f"Average Monthly Profits and Losses: ${averageprofit}")
#print(f"Greatest Increase in Profits: ${maxchange} during {maxmonth}")
#print(f"Greatest Decrease in Profits: ${minchange} during {minmonth}")


with open("PyBank.txt", "w") as text_file:
    
    print(f"Total Months: {month}", file = text_file)
    print(f"Total Profits and Losses: ${totalprofit}", file = text_file)
    print(f"Average Monthly Profits and Losses: ${averageprofit}", file = text_file)
    print(f"Greatest Increase in Profits: ${maxchange} during {maxmonth}", file = text_file)
    print(f"Greatest Decrease in Profits: ${minchange} during {minmonth}", file = text_file)
    
