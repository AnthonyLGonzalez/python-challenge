import csv
from os import read 

## Establish Analysis Variables
MonthList = []
MonthlyAmounts = []
MonthlyDelta = []
NetProfitLoss = 0

## Fetch File Path and Filename
filepath = "/Users/anthonygonzalez/Desktop/GitHub/python-challenge/PyBank/Resources/budget_data.csv"

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
GreatestIncreaseIndex = MonthlyDelta.index(max(MonthlyDelta))
GreatestDecreaseIndex = MonthlyDelta.index(min(MonthlyDelta))

print("Financial Analysis: \n ----------------------------")
print("Total Months: " + str(TotalMonths))
print("Total: $" + str(NetProfitLoss))
print("Average  Change: $" + str(PeriodChangeAverage))
print("Greatest Increase in Profits: " + MonthList[GreatestIncreaseIndex + 1] + " ($" + str(MonthlyDelta[GreatestIncreaseIndex]) + ")")
print("Greatest Decrease in Profits: " + MonthList[GreatestDecreaseIndex + 1] + " ($" + str(MonthlyDelta[GreatestDecreaseIndex]) + ")")





