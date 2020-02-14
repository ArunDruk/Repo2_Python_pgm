# def unique_names(names1, names2):
#     return names1[0],names1[1],names1[2],names2[1]
#
# names1 = ["Ava", "Emma", "Olivia"]
# names2 = ["Olivia", "Sophia", "Emma"]
# i,j,k,l=(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia
# print(i,",",j)
####################################################################################################
l=["Arun","Soumya","sukanya","Arun"]
L=[6,8,2,1]
s=set() # Set removes duplicate entries.
for i in L:
    s.add(i)
print(s)

# files = {
#     'Input.txt': 'Randy',
#     'Code.py': 'Stan',
#     'Output.txt': 'Randy'
# }
# print(files.get("Code.py"))
# #print(files.items())
# # print(files.get("Input.txt"))
# print(files.get("Randy","Key Didn't find"))
#
#   Output of the program should be : {'Stan': ['Code.py'], 'Randy': ['Output.txt', 'Input.txt']}

# def group_owners(files):
#     #result={}
#     ownerdict={}
#     # for filename, owner in files.items():
#     #     result[owner] = result.get(owner, []) + [filename]
#     for key, value in files.items():
#         if value in ownerdict:
#             ownerdict[value].append(key)
#         else:
#             ownerdict[value] = [key]
#     return ownerdict
#
#
#     #return result
#
#
# print(group_owners(files))



