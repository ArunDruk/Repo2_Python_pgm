import pandas as pd
import matplotlib.pyplot as plt
import xlsxwriter
import numpy as np
import xlrd
import xlwt
df1=pd.read_excel('EXAM_results1.xls')
# #print(file.sheet_names)
#print(df1)
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('EXAM_results1.xls', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df1.to_excel(writer, sheet_name='All_subjects')

# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['All_subjects']

# Create a chart object.
chart = workbook.add_chart({'type': 'column'})

# Configure the series of the chart from the dataframe data.
chart.add_series({'values': '=All_subjects!$C$2:$C$18'})

# Insert the chart into the worksheet.
worksheet.insert_chart('F2', chart)

# Close the Pandas Excel writer and output the Excel file.
writer.save()
# #print(df1.head())
#
# #def logic(x):
#   #  x=x*100/100
#
# df1["percentage"]=df1["Total"]
# writer=pd.ExcelWriter('new_book.xls')
# df1.to_excel(writer,'new_sheet')
# writer.save()

# L1=["Arun","Kiran", "Dad", "Mom"]
# L2=[31,33,55,50]
# #family_List=list(zip(L1,L2)) # list concatenation of L1 and L2
# family_List=[["Arun",31],["Kiran",33],("Dad",50)]
# print(type(family_List))
# print(family_List)
# df=pd.DataFrame(data=family_List, columns=["Name","Age"],index=('a','b',"c")) #pandas.DataFrame( data, index, columns, dtype, copy)
# print(df)

# Below is for reading the excel file and converting it as Numpy array - List and storing it to a variable df_np and printing it
# df1=pd.read_excel('EXAM_results1.xls')
# df_np=np.array(df1)
# print ("This is Numpy array : ", df_np)









