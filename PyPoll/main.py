import csv

## Establish Analysis Variables

TotalVoteCount = 0

Votes = {}

VoteList = []

Winner = ""

WinnerValue = 0


## Fetch File Path and Filename
filepath = "/Users/anthonygonzalez/Desktop/GitHub/python-challenge/PyPoll/Resources/election_data.csv"

with open(filepath, 'r') as csvFile:

    csv_data = csv.reader(csvFile,delimiter=",")

    ## Exclude Header data
    csv_header = next(csv_data)
    
    for row in csv_data:
        
        ## Tabulate Total Votes
        TotalVoteCount = TotalVoteCount + 1 
        
        ## Create List of Candidate Votes
        VoteList.append(row[2])

## Create a Dictionary to tally Votes
## Loop through Vote List
for Candidate in VoteList:

   ## If Candidate is in the Dictionary
   if (Candidate in Votes):

      ## Add to current vote count
      Votes[Candidate] = Votes[Candidate] + 1
   
   ## If Candidate is not in the Dictionary
   else:
      
      ## Set Vote Count = 1 
      Votes[Candidate] = 1

## Gather Final Output
print("Election Results: ")
print("-------------------------")
print("Total Votes: " + str(TotalVoteCount))
print("-------------------------")
for key, value in Votes.items():

    print(key + ": " + str( round ( value / TotalVoteCount * 100  , 3 ) ) + "% (" + str(value) + ")" )

    if value > WinnerValue:
        WinnerValue = value
        Winner = key
    
print("-------------------------")
print("Winner: " + Winner)
print("-------------------------")





## Begin CSV Output
output_path = "/Users/anthonygonzalez/Desktop/GitHub/python-challenge/PyPoll/Analysis/Election_Results.csv"

with open(output_path, 'w') as csvoutput:

    # Initialize csv.writer
    csvwriter = csv.writer(csvoutput,delimiter=",")
    
    # # Write analysis to csv file
    csvwriter.writerow(["Election Results: "])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow(["Total Votes: " + str(TotalVoteCount)])
    csvwriter.writerow(["-------------------------"])
    for key, value in Votes.items():

         csvwriter.writerow([key + ": " + str( round( ( value / TotalVoteCount ) * 100 , 3)  ) + "% (" + str(value) + ")" ])

         if value > WinnerValue:
             WinnerValue = value
             Winner = key
    
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow(["Winner: " + Winner])
    csvwriter.writerow(["-------------------------"])