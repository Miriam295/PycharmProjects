import os
import csv
from csv import writer
from csv import reader
#define function to add columns
def add_column_in_csv(input_file, output_file, transform_row):
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        csv_reader = reader(read_obj)
        csv_writer = writer(write_obj)
        for row in csv_reader:
            transform_row(row, csv_reader.line_num)
            csv_writer.writerow(row)
#search for stock data files
stock_head = ('Date,Open,High,Low,Close,Adj Close,Volume')
directory = os.path.join("c:\\", input("Enter the folder to search in: "))
for root,dirs,files in os.walk(directory):
    for file in files:
       if file.endswith(".csv"):
           with open(file, 'r') as stock:
               reader1 = csv.reader(stock)
               if next(reader1) != stock_head:
                   continue
               else:
                   #start calculation
