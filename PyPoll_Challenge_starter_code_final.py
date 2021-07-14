# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os
# Add a variable to load a file from a path.
file_to_load = os.path.join( "Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}
# 1: Create a county list and county votes dictionary.
county_list=[]
county_votes={}
# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_count_1 = 0
winning_percentage = 0
winning_percentage_1 = 0
winning_county = ""
# Read the csv and convert it into a list of dictionaries
# 2: Track the largest county and county voter turnout.
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    header = next(file_reader)
    #print (header)
    for row in file_reader:
        total_votes +=1
        county_name=row[1]
        candidate_name=row[2]
        if county_name not in county_list: 
            county_list.append(county_name)
            county_votes[county_name]= 0
        county_votes[county_name] += 1
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name] +=1
with open (file_to_save, "w") as txt_file:
    election_results = (f"\nElection Results"
        f"\n-----------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------------------\n"
        f"\nCounty Votes:\n")
    print(election_results)
    txt_file.write(election_results)    
    #print (f"\n---------------------------\n" # this is commented out in last stage
           #f" Total Votes : {total_votes:,}\n"
           #f"----------------------------\n")
    for county_name in county_votes:    # Iterating through the county list using county_name as the key and getting the values (votes)
        votes=county_votes[county_name] # Retrieving the total votes for each county using key(county_name), value=votes
        vote_percentage = float(votes) / float (total_votes)* 100 # Calculating the percentage of votes for each county
    # At this point of the above code, we have gone through our dictionary 1 time, getting the county and its vote, before moving down
    # to the If statement, where we check so that vote>0, and will assign our winning vote the first county and its vote in our dictionary list
    #  and check so that it is >0. 
    # After the If statement, we move to the second county in our dictionary list and get its value and compare it again
    # with the if statement below to see which one is greater and assign that to the winning_count
        county_results= (f"{county_name}:{vote_percentage :.1f}% ({votes:,})\n")
        print(county_results)
        txt_file.write(county_results)
        if(votes>winning_count) and (vote_percentage>winning_percentage): #check to make sure that the votes and %votes>0
            winning_count=votes
            winning_percentage = vote_percentage
            winning_county = county_name
    county_winner= (f"\n-----------------------------------\n"
                    f"Largest County Turnout: {winning_county}\n"
                    f"-----------------------------------\n")
    print(county_winner)
    txt_file.write(county_winner)

    for candidate_name in candidate_votes:   #this for loop does the same as the previous, but iterates through the candidate names
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage :.1f}% ({votes:,})\n")
        print(candidate_results) 
        txt_file.write(candidate_results)   
        if(votes>winning_count_1) and (vote_percentage>winning_percentage_1): #we assigned a new winning_count_1 and set that to = 0, since the winning_count
            #used in previous if statement is not 0 by the time the code has got this far
            winning_count_1=votes
            winning_percentage_1 = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"----------------------------------\n"
        f"Winner:{winning_candidate}\n"
        f"Winning Vote Count: {winning_count_1:,}\n"
        f"winning Percentage: {winning_percentage_1:.1f}%\n"
        f"-----------------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)



       

#print(winning_candidate_summary)