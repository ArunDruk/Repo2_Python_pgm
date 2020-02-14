filename = 'Notes.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for i in lines:
    print(i)