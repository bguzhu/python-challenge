#!/usr/bin/env python
# coding: utf-8

# In[37]:


#Needed for reading or writing to csv
import os
import csv

#Define variable to go through data file under Resources folder
budget_csv = os.path.join('.', 'Resources', 'budget_data.csv')

#Define variable to create a file with the final results
analysis_results = os.path.join('.', 'budget_analysis_results.txt')

total_months = 0
total = 0
average_change_list = []

greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999999]

#Include the first month in the month count
total_months += 1

#Read the budget CSV file
with open(budget_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    
    #Looks at the first row and creates it as a list
    header = next(csvreader)
    #Row that includes date and profits/losses 
    first_data = next(csvreader)
    
    total += int(first_data[1])
    previous_average = int(first_data[1])
    
    #Look at every row not including the first_data row
    for row in csvreader:
        total_months += 1
        total += int(row[1])
        average_change = int(row[1]) - previous_average
        previous_average = int(row[1])
        average_change_list.append(average_change)
     
        if (average_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = average_change
            
        if(average_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = average_change
  
    average_changes = sum(average_change_list) / len(average_change_list)
    
results =(  
    f"Financial analysis\n"
    f"----------------------------\n"
    f"Total months: {total_months}\n"
    f"Total: ${total}\n"
    f"Average Change: ${average_changes:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"
)
print(results)

#Writes the results to a file budget_analysis_results.txt
with open(analysis_results, "w") as resultsfile:
    resultsfile.write(results)


# In[ ]:





# In[ ]:




