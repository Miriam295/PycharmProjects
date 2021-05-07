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
