#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Needed to write and read csv files
import os
import csv

#Define variable to go through data file under Resources folder
poll_csv = os.path.join('.', 'Resources', 'election_data.csv')

#Define variable to create a file with the poll results
poll_results = os.path.join('.', 'election_data_results.txt')

total_votecount = 0

voter_votes = {}
voter_list = []

victorious_count = 0
victor = ""

#Read the election CSV file
with open(poll_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Looks at the first row and creates it as a list
    header = next(csvreader)
    
    for row in csvreader:
        total_votecount += 1
        
        voter = row[2]
        
        #checks if the voter is different and adds to the empty list
        if voter not in voter_list:
            voter_list.append(voter)
            
            #Creates a dictionary with voter as a key where values for each voter is set to 0
            voter_votes[voter] = 0
            
        #Increment the count to keep track of the votes  
        voter_votes[voter] += 1

#Writes the results to a file election_data_results.txt
with open(poll_results, "w") as resultsfile:
    results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total votes: {total_votecount}\n"
        f"-------------------------\n"
    )
     
    print(results)
    
    resultsfile.write(results)
    
    for candidate in voter_votes:
        #Counts votes based on each item in the dictionary
        votes = voter_votes[candidate]
        votes_percentage = votes / total_votecount * 100
        
        if (votes > victorious_count):
            victorious_count = votes
            victor = candidate
            
        voter_result = f"{candidate}: {votes_percentage:.3f}% ({votes})\n"
        
        print(voter_result)
        
        resultsfile.write(voter_result)
        
    victor_summary = (
        f"-------------------------\n"
        f"Winner: {victor}\n"
        f"-------------------------\n"
    )
    print(victor_summary)
    
    resultsfile.write(victor_summary)
    


# In[ ]:





# In[ ]:




