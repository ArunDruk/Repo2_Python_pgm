# for i in range(5,0):
#     print(i,end='') #end function prints the output of print function in a single line
# print("Party Starts now ....")
#
# for i in range(4):
#     print("*"*8) #To print a rectangle
#
# for i in range(4):
#     print("*"*(i+2)) #To print a Triangle

# i=1
# while i<15:
#     print (i)
#     i+=2
# print("Last value of i is :",i)

def wrestling(stars,*Heros):
   #for i in Heros:
     print(f'The {stars} are {Heros}') #Formatted output print(f'The stars are {Var1} and {Var2}')


wrestling("wwe_stars","Rock","Kane","Stone_Cold")