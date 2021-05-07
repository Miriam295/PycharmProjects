#I sadly couldnt finalize this
#What's still missing: (I basically only finished assignment 2 and started the rest with flaws):
    #Calculation is only saved for last file in loop (as it currently overwrites the old output)
    #and I tried adding the old data + new column together with next() and .append, but:
        #when adding, the date is pasted to the end a second time;
        #the first two rows somehow disappeared;
        #the calculated change does not change with the rows

#search for stock data files and apply function
import csv
from pathlib import Path

csv_data = Path(input("Enter the full path to search in: ")).rglob('*.csv')
files = [x for x in csv_data]
stock_files = []
for file in files:
    file_str = str(file)
    if file_str.endswith(".csv"):
        with open(file_str, 'r') as stock:
            reader1 = csv.reader(stock)
            stock_head = str(['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
            test = str(next(reader1))
            if test == stock_head:
                stock_files.append(file)

for el in stock_files:
    print(el)
    with open(el, 'r') as input:
        with open('stock_with_change.csv', 'w', newline = '') as output:
            reader = csv.reader(input)
            writer = csv.writer(output)
            i = 0
            change_collect = []
            for line in reader:
                i += 1
                if i > 1:
                    for k in range(1, 7):
                        line[k] = float(line[k])
                    change = ((line[4] - line[1]) / line[1])
                    change_collect += [change]
                    all = []
                    row = next(reader)
                    row.append('Change')
                    all.append(row)
                    for row in reader:
                        for row2 in change_collect:
                            row.append(row2)
                            all.append(row)
            writer.writerows(all)

print(change)
print(change_collect)
print(len(change_collect))
print('----')
print(all)
print(len(all))