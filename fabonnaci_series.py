# !/usr/bin/local/python3

no=int(input("enter number till u want fabonnaci series : "))


def fabonnaci_number(n):

    if n==0:
        return 0
    elif n==1:
        return 1
    return fabonnaci_number(n-1)+fabonnaci_number(n-2)

for i in range(no):
   
    print(fabonnaci_number(i))
    print(end=" ")
    


