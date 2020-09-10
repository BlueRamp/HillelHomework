try:
    x = float(input("Input x:"))
    y = float(input("Input y:"))
except ValueError as error:
    print(error)
day = 1
while x != 0:
    if y <= x:
        print(day)
        break
    else:
        x += x * 1.1
        day += 1