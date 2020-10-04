natural_number = int(input("Input natural number:"))
if natural_number > 0:
    if natural_number % 4 == 0 and natural_number % 100 != 0 or natural_number % 400 == 0:
        print("YES")
    else:
        print("NO")
else:
    print("It's not natural number")
