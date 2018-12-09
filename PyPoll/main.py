import os

import csv


# Path to collect data from the Resources folder
pypoll_csv = os.path.join('.', 'Resources', 'election_data.csv')

# Read in the CSV file
with open(pypoll_csv, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    
    numvotes = 0
    numkhan = 0 
    numli = 0
    numcorrey = 0
    numotool = 0
    winner = ""
    Lcandidates = []
    Allcandidates = {}
    voteWinner = ""
    
    for row in csvreader:
        Candidate = str(row[2])
        if not any(Candidate in currentcand for currentcand in Lcandidates):
            Lcandidates.append(Candidate)
            Allcandidates.update({Candidate: 0})
    numvotes = numvotes +1
# Path to collect data from the Resources folder
pypoll_csv = os.path.join('.', 'Resources', 'election_data.csv')

# Read in the CSV file
with open(pypoll_csv, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)

    print(Lcandidates)

    for row in csvreader:
        Candidate = str(row[2])
        
        if Candidate == Lcandidates[0]:
            numkhan = numkhan + 1
            Allcandidates.update({Candidate: numkhan})

        elif Candidate == Lcandidates[1]:
            numcorrey = numcorrey + 1
            Allcandidates.update({Candidate: numcorrey})
            
        elif Candidate == Lcandidates[2]:
            numli = numli + 1
            Allcandidates.update({Candidate: numli})
            
        elif Candidate == Lcandidates[3]:
            numotool = numotool + 1
            Allcandidates.update({Candidate: numotool})

voteWinner = max(Allcandidates.values())

maxCand = [k for k,v in Allcandidates.items() if v == voteWinner]


pctKhan = round(numkhan/numvotes*100,2)
pctCorrey = round(numcorrey/numvotes*100,2)
pctLi = round(numli/numvotes*100,2)
pctOtooley = round(numotool/numvotes*100,2)


print("Election Results")
print(" ----------------------------")
print(f"Total Votes    :   {numvotes}")
print(f" ----------------------------")
print(f"{Lcandidates[0]}    :   {pctKhan}% ({numkhan})")
print(f"{Lcandidates[1]}    :   {pctCorrey}% ({numcorrey})")
print(f"{Lcandidates[2]}    :   {pctLi}% ({numli})")
print(f"{Lcandidates[3]}    :   {pctOtooley}% ({numotool})")
print(f" ----------------------------")
print(f" Winner : {maxCand}")
print(f" ----------------------------")

with open("PyPoll.txt", "w") as text_file:
    print("Election Results", file=text_file)
    print(" ----------------------------", file=text_file)
    print(f"Total Votes    :   {numvotes}", file=text_file)
    print(f" ----------------------------", file=text_file)
    print(f"{Lcandidates[0]}    :   {pctKhan}% ({numkhan})", file=text_file)
    print(f"{Lcandidates[1]}    :   {pctCorrey}% ({numcorrey})", file=text_file)
    print(f"{Lcandidates[2]}    :   {pctLi}% ({numli})", file=text_file)
    print(f"{Lcandidates[3]}    :   {pctOtooley}% ({numotool})", file=text_file)
    print(f" ----------------------------", file=text_file)
    print(f" Winner : {maxCand}", file=text_file)
    print(f" ----------------------------", file=text_file)   
        
 
