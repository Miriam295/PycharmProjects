#function that calculates file sizes in folder
import os
folder = input('Enter folder path: ')
print("For folder", folder, ":")

#part 1: total size of folder
def sum_space(folder):
    total_size = 0
    for item in os.listdir(folder):
        path = os.path.join(folder, item)
        if os.path.isfile(path):
            total_size += os.path.getsize(path)
        elif os.path.isdir(path):
            total_size += sum_space(path)
    return total_size

print("Total space occupied by folder: " + str(sum_space(folder)) + " bytes")

#part 2: number of files in folder

def sum_count(folder):
    count = 0
    for item in os.listdir(folder):
        path = os.path.join(folder, item)
        if os.path.isfile(path):
            count += 1
        elif os.path.isdir(path):
            count += sum_count(path)
    return count

print("Number of files in this folder: " + str(sum_count(folder)) + " folder(s)")