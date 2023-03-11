
#Modules
import os
import csv


#set path to fin csv file location
budget_data_path = os.path.join('Resources', 'budget_data.csv')


#naming variables to set as lists
Date_list =[]
Profit_loss_list = []
Monthly_change=[] 
#set variables to zero
Average_changes=0
greatest_decrease= 0
greatest_increase=0
greatest_decrease_date=0
greatest_increase_date=0

#open csv file using path created above
with open(budget_data_path) as csvfile:
    
    #open reader of csv file 
    budgetreader = csv.reader(csvfile,delimiter=',')
    #skip header row
    header = next (budgetreader)  

    #loop through each row of csv file
    for row in budgetreader:
        #and turn all data in first column called Date of CSV file into a list
        Date_list.append(row[0]) 
        #and turn all data in second column called Profit/Losses of CSV file into a list
        Profit_loss_list.append(int(row[1]))

#loop through total Profit_loss_list 
for i in range(len(Profit_loss_list)-1):
        #create new list that calculates month to month changes by subtracting current month by previous month
        Monthly_change.append(Profit_loss_list[i+1]-Profit_loss_list[i])

#Calculate average change by adding sum of monthly profit changes and dividing it by total number of months
Average_changes = sum(Monthly_change)/len(Monthly_change)

#find the max and min values in monthly profit changes list to identify greatest increase and decrease in profit
greatest_decrease = min(Monthly_change)
greatest_increase = max(Monthly_change)

#Set index for greatest increase and decrease in profit values to later find corresponding Date with each value     
greatest_decrease_date=Monthly_change.index(min(Monthly_change))+1
greatest_increase_date=Monthly_change.index(max(Monthly_change))+1

print(f'Financial Analysis')
print('------------------------------------')
#print total number of months 
print (f'Total Months: {(len(Date_list))}')
#print net total by adding all values in Profit/Losses column 
print(f'Total: ${(sum(Profit_loss_list))}')
#print average change and round value to 2 decimal spots
print(f'Average Change: ${round(Average_changes,2)}')
#Print date and value of greatest decrease in profit. locate date by using index value of greatest decrease profit amount and find corresponding date
print(f'Greatest Decrease in Profits: {(Date_list[greatest_decrease_date])} ${greatest_decrease}')
#Print date and value of greatest increase in profit. locate date by using index value of greatest increase profit amount and find corresponding date
print(f'Greatest Increase in Profits: {(Date_list[greatest_increase_date])} ${greatest_increase}')

with open("analysis/PyBank_Analysis.txt", 'w')as text:
                            
        text.write('Financial Analysis\n')
        text.write('------------------------------------\n')
        text.write('Total Months:' + str(len(Date_list)) + '\n')
        text.write('Total: $' + str(sum(Profit_loss_list)) + '\n')
        text.write('Average Change: $' + str(round(Average_changes,2)) + '\n')
        text.write('Greatest Decrease in Profits: ' + str(Date_list[greatest_decrease_date]) + ' $' + str(greatest_decrease) +'\n')
        text.write('Greatest Increase in Profits: ' + str(Date_list[greatest_increase_date]) + ' $' +str(greatest_increase) + '\n')
        