number_a = int(input("Input A:"))
number_b = int(input("Input B:"))
some_list = []
if number_a < number_b:
    for i in range(number_a, number_b+1):
        some_list.append(i)
    print(some_list)
if number_a > number_b:
    for k in range(number_b, number_a+1):
        some_list.append((number_a + 1) - k)
    print(some_list)