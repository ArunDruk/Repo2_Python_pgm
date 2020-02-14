import math
import functions #This is imported from the file functions.py from the same directory.
import sys
from importlib import reload
sys.path.append("C:\Python_Programs") # to import a module which is in someother directory.
#import Functions

print(math.sqrt(2))
#print(dir(math)) #prints all the funtions inside the module math
#reload(functions)
print(functions.print_square("This block of code is from modules"))

#print(Functions.my_function("ARUN"))



