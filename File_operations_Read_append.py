with open("sample1.txt","r+") as fr:
    a=fr.readline()
    fr.write("\n")
    fr.write("This am writing from the python code.\n")
    b=fr.readline()

print(a)
print(b)