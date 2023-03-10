#Modules
import os
import csv

#set path to fin csv file location
election_data_path = os.path.join('Resources', 'election_data.csv')

Total_votes = []
Candidates_list = []
Candidates_rec_votes= []
Cand_total_votes=[]
Vote_percentage=[]


#open csv file using path created above
with open(election_data_path) as csvfile:
    #open reader of csv file as dictionary
    electionreader = csv.reader(csvfile,delimiter=',')
    header = next (electionreader)  

    for row in electionreader:
        Total_votes.append(row[0])
        Candidates_list.append(row[2])

    for i in set(Candidates_list):
        Candidates_rec_votes.append(i)
        
        total_votes_cand=Candidates_list.count(i)
        Cand_total_votes.append(total_votes_cand)
        
        percentage_vote= (total_votes_cand/len(Total_votes)) *100
        Vote_percentage.append(percentage_vote)
        
    print(f'Election Results')
    print('------------------------------------')
    print (f'Total Votes: {len(Total_votes)}')
    print('------------------------------------')
    print(f'{Candidates_rec_votes[0]}: {round(Vote_percentage[0],2)}%, ({Cand_total_votes[0]})')
    print(f'{Candidates_rec_votes[2]}: {round(Vote_percentage[2],2)}%, ({Cand_total_votes[2]})')
    print(f'{Candidates_rec_votes[1]}: {round(Vote_percentage[1],2)}%, ({Cand_total_votes[1]})')
