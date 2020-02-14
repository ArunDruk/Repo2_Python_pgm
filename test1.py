# import pandas as pd
# h=[['a',1],['b',2],['c',4]]
# s=pd.DataFrame(data=h,index=('i','ii','iii'),columns=("character","Num"))
# print(s)



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# df1=pd.read_excel('EXAM_results1.xls')
# #print(df1)
# #s=df1.describe()
# plt.xlabel('Subjects')
# plt.ylabel('Score')
# #plt.figure()
# #plt.title("MBA_results")
# plt.plot(df1['Total'])
# plt.show(block=True)
# plt.interactive(False)

# x=[1,2,3,4,5]
# y=[1,4,9,16,25]
# z=[25,16,9,4,1]
# plt.xlabel("X-axis")
# plt.ylabel("Y and Z axis")
# plt.title("Square root")
# plt.plot(x,y,'r--')
# plt.plot(x,z,'g:')
# plt.legend(["This is y-data","This is Z-data"])
# plt.show(block=True)
# plt.interactive(False)

x=["Goo","Ama","mic","flip","LG"]
xpos=np.array(len(x))
#print(type(x),type(xpos))
#xpos=len(x)
# print(type(xpos))
print(xpos)
y=[1,4,9,16,25]
z=[1,3,6,12,20]
plt.xticks(xpos,x)
# print("Length of list y: ",len(y))
# plt.title("Square root of numbers")
# plt.xlabel("Number")
# plt.ylabel("Squares of Number")
# #plt.legend("For Num")
plt.bar(xpos,y,width=0.4)
# plt.bar(xpos+0.2,z,width=0.4)
# plt.savefig("myfirstBAR.png",dpi=600)