N=int(input("Input natural number:"))
if N>0:
    if N%4==0 and N%100!=0 or N%400==0:
        print("YES")
    else:
        print("NO")
else:
    print("It's not natural number")
