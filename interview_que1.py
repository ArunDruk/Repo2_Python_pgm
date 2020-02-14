#666322
n1="6662224"
i=0
j=1
count=1
n2=""
for z in range(len(n1)):
    if((n1[i])==n1[j]):
       while (n1[i] == n1[j]):
            count+=1
            n2="".join(n1[k] for k in range(count))+str(count)#+n2
            i+=1
            j+=1
       i,j=2,3
    #print(i,j)

print(n2)

# n="6"
# i="1"
# f=str(1353)+str(6)
# print(f)

# n1="66612"
# #n2=666312
# count=3
# n2="".join(n1[i] for i in range(count))+str(count)
# print(n2)
# c=1
# n2=n2+n1[len(n2)-1]+str(c)
# print(n2)
