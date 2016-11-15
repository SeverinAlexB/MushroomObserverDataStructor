from os import listdir
from os.path import join
from shutil import rmtree


folder_path = '/home/severin/Downloads/mushroom_dataset/'

count = 0
for folder in listdir(folder_path):

    joined = join(folder_path, folder)
    print(joined)
    files_count = listdir(joined)
    print(len(files_count))
    count += 1
    if count > 10:
        exit()

