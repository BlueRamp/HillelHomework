numbers = list(input("Input number:"))
result = 0
for i in range(len(numbers)):
    result = result + int(numbers[i])
print(result)