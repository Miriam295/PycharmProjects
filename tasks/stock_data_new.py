import os
import csv

#search for stock data files
stock_head = ('Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume')
directory = os.path.join("c:\\", input("Enter the folder to search in: "))
for files in os.walk(directory):
    for file in files:
        if file.endswith(".csv"):
            with open(file, 'r') as stock:
                reader1 = csv.reader(stock)
                if next(reader1) != stock_head:
                    continue
                else:
                    with open (file, 'a'):
                        reader2 = csv.reader(stock)
                        for line in reader1: ###need to somehow skip row 1
                            line.append(((line[4] - line[1]) / line[1]))