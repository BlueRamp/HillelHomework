Elements=(10,20,30,40,50,60,70,80,90,100)
x=abs(float(input("input x:")))
i=0
for i in range(10):
    if x==Elements[i]:
        print("x is element",i)
    else:
        i=i+1
