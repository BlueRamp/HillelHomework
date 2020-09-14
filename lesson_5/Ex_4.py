import random
some_list = [random.randint(1, 10) for i in range(10)]
print(some_list)
for k in range(len(some_list)):
    if float(some_list[k]) % 2 != 0:
        some_list[k] = 0
print(some_list.count(0))