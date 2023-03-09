
#Modules
import os
import csv
from statistics import mean

#set path to fin csv file location
budget_data_path = os.path.join('Resources', 'budget_data.csv')


#naming variables to set as lists
Date_list =[]
Profit_loss_list = []
Monthly_change=[] 
Date_change= []
Average_changes=0
greatest_decrease= 0
greatest_increase=0
greatest_decrease_date=0
greatest_increase_date=0
#open csv file using path created above


with open(budget_data_path) as csvfile:
    
    #open reader of csv file as dictionary
    budgetreader = csv.DictReader(csvfile,delimiter=',')
   
    

    #loop through each row of csv file
    for row in budgetreader:
        #and turn all data in first column called Date of CSV file into a list
        Date_list.append(row["Date"]) 
        #and turn all data in second column called Profit/Losses of CSV file into a list
        Profit_loss_list.append(int(row["Profit/Losses"]))
        
     
for i in range(len(Profit_loss_list)-1):
        Monthly_change.append(Profit_loss_list[i+1]-Profit_loss_list[i])
        Average_changes = mean(Monthly_change)
        Date_change= [Date_change] + [row["Date"]]
        
        greatest_decrease = min(Monthly_change)
        
     
        greatest_increase = max(Monthly_change)
     
 
print(f'Financial Analysis')
print('------------------------------------')
#print total number of months 
print (f'Total Months: {(len(Date_list))}')
print(f'Total: ${(sum(Profit_loss_list))}')
print(f'Average Change: ${round(Average_changes,2)}')
print(f'Greatest Decrease in Profits: ${greatest_decrease}')
print(f'Greatest Increase in Profits: ${greatest_increase}')