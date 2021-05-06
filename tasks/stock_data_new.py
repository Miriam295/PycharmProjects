#Program that searches for Stock data files
import csv

#for ... if file is csv and if row 1 line 1 = "date" --> program; else pass

#Calculate percentage change (for each of the found files)
    #change = (close-open) / open
import os.path
print(os.path.exists('IBM.csv'))

with open('TSLA.csv', 'r') as stock:
    read = csv.reader(stock)
    lines = stock.readlines()
    for line in lines:
        i = i + 1
        print("%i: %s" % (i, line))

#filename.append for changing?

#Save output files to another folder