v=int(input("Input velocity:"))
t=int(input("Input time"))
s=v*t
if s<=100 and s>0:
    if s==100:
        print("Vasya is on ", s,"km", "Congrats! You won!")
    else:
        print("Vasya is on ",s,"km")
else:
    print("Impossible")
