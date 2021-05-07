#function that calculates file sizes in folder
import os
f = 'C:/Users/Miriam/PycharmProjects/tasks'
g = 'C:/Users/Miriam/PycharmProjects/tasks/bytes'

#use:
print(os.path.getsize(f))
print(os.listdir(f))

#trial and error
names = os.listdir(f)
print(names)

#https://stackoverflow.com/questions/1392413/calculating-a-directorys-size-using-python

import os
def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size

print(get_size(g), 'bytes')

print('-----time for recursive ----')

import os
def getFolderSize(folder):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size

print("Size: " + str(getFolderSize(g)) + " bytes")
