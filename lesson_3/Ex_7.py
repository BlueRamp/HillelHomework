number = int(input("Input number to find it's factorial:"))
factorial = 1
for i in range(number):
    factorial = factorial * (i+1)
print(factorial)
