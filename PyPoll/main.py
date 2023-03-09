#Modules
import os
import csv

#set path to fin csv file location
election_data_path = os.path.join('Resources', 'election_data.csv')

Total_votes = []
County= []
Candidate = []

#open csv file using path created above
with open(election_data_path) as csvfile:
    #open reader of csv file as dictionary
    electionreader = csv.reader(csvfile,delimiter=',')
    header = next (electionreader)  

    for row in electionreader:
        Total_votes.append(row[0])
    

            

    print(f'Election Results')
    print('------------------------------------')
    print (f'Total Votes: {(len(Total_votes))}')
    print('------------------------------------')
  
