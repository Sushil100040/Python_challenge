import os
import csv

#set the path to the csv file
csvpath = os.path.join('Resources','budget_data.csv')

#open the csv file and read through the rows
with open(csvpath) as budget_data:
    reader = csv.reader(budget_data, delimiter=',')

    #counter for the total of the months
    #skip the header row
    header = next(reader)

    #variables
    count = 0
    total = 0
    net_change = 0
    highloss = 0
    highprofit = 0
    average_net_change = 0
    profitlossdate = ""
    lossdate = ""
    prev_profit_loss = 0

    #iterate through the row of the csv file
    for row in reader:
        profit_losses = int(row[1])
        total += profit_losses
        count += 1

        #calcualte the net change
        if count>1:
            net_change += profit_losses - prev_profit_loss

        #update the high profit and high loss values
        if profit_losses - prev_profit_loss > highprofit:
                highprofit = profit_losses - prev_profit_loss
                profitdate = str(row[0])

        if profit_losses - prev_profit_loss < highloss: 
                highloss = profit_losses - prev_profit_loss
                lossdate = str(row[0])
        
        #update the previous profit/loss value
        prev_profit_loss = profit_losses

    #calculate the average net change
    average_net_change = round(net_change/(count -1),2)
    #generate output summary
    output = (
        f"Financial Analysis\n"
        f"--------------------------\n"
        f"Total Months: {count}\n"
        f"Total: ${total}\n"
        f"Average Change: ${average_net_change}\n"
        f"Greatest Increase in Profits: {profitdate}  (${highprofit})\n"
        f"Greatest Decrease in Profits: {lossdate}   (${highloss})"
    )

#print the output(to terminal)
print(output)
#export the result to text file
#export the result to text file
output_file = os.path.join('resources','analysis.txt')
with open(output_file,"w") as txt_file:
    txt_file.write(output)