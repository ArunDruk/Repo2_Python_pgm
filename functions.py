##############################################################################################
#To print a square

# def print_square(b):
#     print(type(b))
#     print('*'*15)
#     print("*", " " *10, b,'*')
#     print("*", " " *10, b, '*')
#     print('*' *75)
#     return "ARUN"
# print_square("This block contains ..")
############################################################################################
#Generator series
import random
import types

# def lottery():
#     # returns 6 numbers between 1 and 40
#     for i in range(0,6):
#         yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    #yield random.randint(1,15)

# y=lottery()
# for i in range(0,6):  #Generator is compliant with For loop for the iterator without using next y for i in lotery()
#     print(next(y))


# for random_number in lottery():
#        print("And the next number is...", random_number)

########################################################################################
# #MAP function
# l=[("Arun",29),("Sharmila",25)]
# c_to_f=lambda x:(x[0],((9/5)*x[1])+32)
# l2=list(map(c_to_f,l))
# print(l2)

###########################################################################################

# def fib():
#     pass
# import types
# if type(fib()) == types.GeneratorType:
#     print("Good, The fib function is a generator.")

###########################################################################################

# def scope_of_variable():
#     global x,y
#     x=5
#     y=6
#     return x,y
#
# a,b=scope_of_variable()
# print(a,b)
# print(x,y)
###########################################################################################
# def outer():
#     x=5
#     y=x+1
#     def inner():
#        x=5
#        y=x+3
#        return y
#     inner()
#     return y
#
# print(outer())

