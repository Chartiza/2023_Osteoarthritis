#rename_motus_results.py

filename = "VVHM1U.motus" # specify the filename
new_phrase = filename.split('.')[0] # extract the name before the dot
with open(filename, 'r') as file:
    filedata = file.read()

# replace the phrase 'unnamed sample' with the new name
newdata = filedata.replace('unnamed sample', new_phrase)

# write the modified data back to the file
with open(filename, 'w') as file:
    file.write(newdata)
