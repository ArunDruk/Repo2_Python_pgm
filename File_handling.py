#s= open('C:/Users/Admin/PycharmProjects/Pratice_Pgms/Notes.txt').read() #Open a file and assign as a String
#print(s)
#lines=[open('Notes.txt').read()]
#lines=[var.strip() for var in open('Notes.txt')] # store each line of the file as a list, line-by-line
#print(lines[0],end='')
#print(lines[1],end='')
#print(lines[2])
#print("The length of the list is : ",len(lines))

#Below is the string comparison in the file Notes.txt
# src_str=open("Notes.txt").read()
# a_bool="important" in src_str #Search for a word in a string, if present it will return True else False
# print(a_bool)
# #print(type(src_str))
# #print(src_str)
# if (a_bool==True):
#     print("The file contains Important")
# else:
#      print("The file doesn't contain the word important")

# fb=[open("Notes.txt").readlines()]
# #lines=fb.readlines()
#
# for i in fb:
#     print (i)

filename = 'Notes.txt'
with open(filename,'r') as file_read:
    lines = file_read.readlines()
#print(type(lines))
for i in lines:
    print(i,end='')

with open(filename,'a') as file_append:
     file_append.write("This line is added by appending the file and opening in append mode")




