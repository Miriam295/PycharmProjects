#Program that searches for Stock data files


#Calculate percentage change (for each of the found files)
    #change = (close-open) / open
import csv
with open('TSLA.csv', 'w') as stock:
    read = csv.reader(stock)
    for row in stock:
        print row



#Save output files to another folder
