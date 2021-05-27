#updated: now calculates and displays the change correctly, saves it in different files for different datasets
#Sorry for the delay, I appreciate the chance to correct the exercise!

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

#calculating change rate and adding it to new column
i = 0
for el in stock_files:
    #print(el)
    names = []
    for n in range(len(stock_files)):
        if n == i:
            name = f'stock_with_change{n}.csv'
            names += [name]
            #print(names)
        else:
            pass
    with open(el, 'r') as input:
        name2 = names[-1]
        #print(name2)
        with open(name2, 'w', newline='') as output:
            reader = csv.reader(input)
            writer = csv.writer(output)
            header = next(reader)
            change_collect = []
            all = []
            for line in reader:
                if header != None:
                    for k in range(1, 7):
                        line[k] = float(line[k])
                    change = ((line[4] - line[1]) / line[1])
                change_collect.append(change)
                for index in range(len(change_collect)):
                    line.append(change_collect[-1])
                    all.append(line)
                    break
            writer.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Change'])
            writer.writerows(all)
        print(f'\n Idenfitied stock data file: {el}. \n Calculated change can be found in "{name2}" \n')
    i = i+1