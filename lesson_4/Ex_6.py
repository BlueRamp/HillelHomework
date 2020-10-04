some_list = [int(i) for i in input("Enter numbers separated by spaces and press Enter:").split()]
count = 0
j = 1
while j < len(some_list):
    if some_list[j] > some_list[j-1] and some_list[j] > some_list[j+1]:
        count += 1
    j += 1
print(count)