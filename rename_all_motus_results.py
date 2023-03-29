#rename_all_motus_results.py

import os

directory = '/gpfs/space/home/pantiukh/2023_Osteoarthritis/motus/all' # specify the directory containing the files

for filename in os.listdir(directory):
    if filename.endswith('.motus'): # only process files with .motus extension
        filepath = os.path.join(directory, filename)
        new_phrase = filename.split('.')[0]
        with open(filepath, 'r') as file:
            filedata = file.read()
        newdata = filedata.replace('unnamed sample', new_phrase)
        with open(filepath, 'w') as file:
            file.write(newdata)
