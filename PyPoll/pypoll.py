# Import necessary packages to execute the code
import os
import csv

# Create a filepath to pull data from csv
filepath = os.path.join("Resources","election_data.csv")

# Create necessary lists to store data
candidates_names = []

# Set necessary counters to keep count
vote_count = 0

Khan_votes = 0
Correy_votes = 0
Li_votes = 0
O_votes = 0

# Open the file using with command to run the code
with open(filepath,"r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)


# Create for loop to run code through each row
    for row in csvreader:

        #candidates_list.append(str(row[2]))

#   The total number of votes cast
        vote_count += 1

#   A complete list of candidates who received votes
        #candidates_set.add(row[2])

        candidates_names.append(str(row[2]))

#   The percentage of votes each candidate won

#   The total number of votes each candidate won
    for name in candidates_names:
        if name == "Khan":
                Khan_votes += 1
                Khan_vote_percentage = round((Khan_votes/vote_count)*100,2)
        if name == "Correy":
                Correy_votes += 1
                Correy_vote_percentage = round((Correy_votes/vote_count)*100,2)    
        if name == "Li":
                Li_votes += 1
                Li_vote_percentage = round((Li_votes/vote_count)*100,2)
        if name == "O'Tooley":
                O_votes += 1
                O_vote_percentage = round((O_votes/vote_count)*100,2)
       
#   The winner of the election based on popular vote.
winner = max(set(candidates_names), key=candidates_names.count)

# Print results

print(f'''
  
    Election Results
    -------------------------
    Total Votes: {vote_count}
    -------------------------
    Khan: {Khan_vote_percentage}% ({Khan_votes})
    Correy: {Correy_vote_percentage}% ({Correy_votes})
    Li: {Li_vote_percentage}% ({Li_votes})
    O'Tooley: {O_vote_percentage}% ({O_votes})
    -------------------------
    Winner: {winner}
    -------------------------
    ''')


# Export to txt file
final_results = "final_results.txt"
with open(final_results,"w") as results:
    results.write(f'''
  
    Election Results
    -------------------------
    Total Votes: {vote_count}
    -------------------------
    Khan: {Khan_vote_percentage}% ({Khan_votes})
    Correy: {Correy_vote_percentage}% ({Correy_votes})
    Li: {Li_vote_percentage}% ({Li_votes})
    O'Tooley: {O_vote_percentage}% ({O_votes})
    -------------------------
    Winner: {winner}
    -------------------------
    ''')