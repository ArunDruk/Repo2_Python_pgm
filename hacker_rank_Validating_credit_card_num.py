import re
card_num=input("Enter your Credit Card Num: ")

if len(card_num)==16:
    a=re.search(r'([[456]{1,3}\-\d])',card_num)
    if a.group() !=None:
        print("Valid")
    else:
        print("Invalid")



