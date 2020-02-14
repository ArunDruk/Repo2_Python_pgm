# from functools import reduce
#
# my_list=[]
# for i in range (0,21):
#     my_list.append(i)
#
# even_list=list(filter(lambda e:e%2==0,my_list))
# even_list_adding=reduce(lambda x,y:x+y,even_list)
#
# print(even_list)
# print(type(even_list_adding),even_list_adding)

name_age=[("Arun",23),("Deepa",28)]
add8=lambda x: (x[0] + "KUMAR",(x[1]+8))
modified=list(map(add8,name_age))
print(modified)