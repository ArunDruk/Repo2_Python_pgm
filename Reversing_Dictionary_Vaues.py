D={1:'a',2:('aa','bb'),3:33}
print("Given Dictionary is : ",D)
L1=[]
L=D.values()
for i in L:
     L1.append(i)
L1.reverse()

b=0
for k in D.keys():
    D[k]=L1[b]
    b+=1

# print(L1,type(L1))
print("Reversing the values of the Dictionary",D,type(D))