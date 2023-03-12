#Modules
import os
import csv

#set path to find csv file location
election_data_path = os.path.join('Resources', 'election_data.csv')

#set variables for lists
Total_votes = []
Candidates_list = []
Candidates_rec_votes= []
Cand_total_votes=[]
Vote_percentage=[]


#open csv file using path created above
with open(election_data_path) as csvfile:
    #open reader of csv file 
    electionreader = csv.reader(csvfile,delimiter=',')

    #skip header line
    header = next (electionreader)  

    #loop through each row of csv file data
    for row in electionreader:
        #Make a list with all votes from data in first row of CSV file
        Total_votes.append(row[0])
        #Make a list of candidates from data in third row of CSV file
        Candidates_list.append(row[2])

    #loop through Candidates list created above to find unique data
    for i in set(Candidates_list):
        #list of names of all candidates that received votes
        Candidates_rec_votes.append(i)
        Candidates_rec_votes.index
        
        #list that counts how many votes each unique candidate received
        total_votes_cand=Candidates_list.count(i)
        Cand_total_votes.append(total_votes_cand)
        Cand_total_votes.index

        #list of calculated percentage of votes each candidate 
        percentage_vote= (total_votes_cand/len(Total_votes)) *100
        Vote_percentage.append(percentage_vote)
        Vote_percentage.index
        
    #locate index of max value for popular votes to correlate candidate name with most popular votes
    Winner= Cand_total_votes.index(max(Cand_total_votes))

        
print(f'Election Results')
print('-----------------------------------')
#print total votes
print (f'Total Votes: {len(Total_votes)}')
print('------------------------------------')
#print Canadidate name, vote percentage, total votes, for each candidate
print(f'{Candidates_rec_votes[0]}: {round(Vote_percentage[0],2)}%, ({Cand_total_votes[0]})')
print(f'{Candidates_rec_votes[2]}: {round(Vote_percentage[2],2)}%, ({Cand_total_votes[2]})')
print(f'{Candidates_rec_votes[1]}: {round(Vote_percentage[1],2)}%, ({Cand_total_votes[1]})')
print('------------------------------------')
#print winner name using index max(most popular votes) to find name
print(f'The Winner is: {(Candidates_rec_votes[Winner])}')
print('------------------------------------')

with open("analysis/PyPoll_Analysis.txt", 'w')as text:
    text.write('Election Results\n')
    text.write('-----------------------------------\n')
    text.write('Total Votes: ' + str(len(Total_votes)) +'\n')
    text.write('------------------------------------\n')
    text.write(str(Candidates_rec_votes[0]) + ': ' + str(round(Vote_percentage[0],2)) + '% (' + str(Cand_total_votes[0]) + ')\n')
    text.write(str(Candidates_rec_votes[2]) + ': ' + str(round(Vote_percentage[2],2)) + '% (' + str(Cand_total_votes[2]) + ')\n')
    text.write(str(Candidates_rec_votes[1]) + ': ' + str(round(Vote_percentage[1],2)) + '% (' + str(Cand_total_votes[1]) + ')\n')
    text.write('------------------------------------\n')
    text.write('The Winner is: ' + str(Candidates_rec_votes[Winner])+ '\n')
    text.write('------------------------------------')