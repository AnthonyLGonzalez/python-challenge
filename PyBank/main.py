import csv
from os import read 

## Establish Analysis Variables
MonthList = []
MonthlyAmounts = []
MonthlyDelta = []
NetProfitLoss = 0

## Fetch File Path and Filename
filepath = "python-challenge/PyBank/Resources/budget_data.csv"

## Begin CSV Reader
with open(filepath,'r') as csvFile:

    ## Read File
    csv_data = csv.reader(csvFile,delimiter=",")

    ## Skip Header Row
    csv_header = next(csvFile)

    ## Iterate through CSV File
    for row in csv_data:

        ## Create a list of Months
        MonthList.append(row[0])

        ## Create a list of $ Amounts for each month
        MonthlyAmounts.append(row[1])

        ## Sum Profit / Loss for each month to calculate Net Amount
        NetProfitLoss = NetProfitLoss + int(row[1])


TotalMonths = len(MonthlyAmounts)

## Begin Calculate Month over Month Delta
rowNum = 0

# Loop through each Monthly Amount beginning at the 2nd item and build a list
for x in range(1,len(MonthlyAmounts)):

  # Calculate Current Month Amount - Previous Month Amount
  MonthlyDelta.append(int(MonthlyAmounts[x]) - int(MonthlyAmounts[rowNum]) )

  # Add to RowNum to keep month over month calculation in line
  rowNum = rowNum + 1

PeriodChangeAverage = round(sum(MonthlyDelta) / len(MonthlyDelta),2)

## Fetch Greatest Increase/Decrease by using index on Zipped List
Increase = MonthlyDelta.index(max(MonthlyDelta))
Decrease = MonthlyDelta.index(min(MonthlyDelta))

zip_MonthChange = list(zip(MonthList[1:TotalMonths],MonthlyDelta))

## Begin Terminal Output
print("Financial Analysis: \n ----------------------------")
print("Total Months: " + str(TotalMonths))
print("Total: $" + str(NetProfitLoss))
print("Average  Change: $" + str(PeriodChangeAverage))
print("Greatest Increase in Profits: " + zip_MonthChange[Increase][0] + " ($" + str(zip_MonthChange[Increase][1]) + ")")
print("Greatest Decrease in Profits: " + zip_MonthChange[Decrease][0] + " ($" + str(zip_MonthChange[Decrease][1]) + ")")

## Begin CSV Output
output_path = "python-challenge/PyBank/Analysis/FinancialAnalysis.csv"

with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile,delimiter=",")

    # Write analysis to csv file
    csvwriter.writerow(["Financial Analysis:"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(["Total Months: " + str(TotalMonths)])
    csvwriter.writerow(["Total: $" + str(NetProfitLoss)])
    csvwriter.writerow(["Average  Change: $" + str(PeriodChangeAverage)])
    csvwriter.writerow(["Greatest Increase in Profits: " + zip_MonthChange[Increase][0] + " ($" + str(zip_MonthChange[Increase][1]) + ")"])
    csvwriter.writerow(["Greatest Decrease in Profits: " + zip_MonthChange[Decrease][0] + " ($" + str(zip_MonthChange[Decrease][1]) + ")"])
