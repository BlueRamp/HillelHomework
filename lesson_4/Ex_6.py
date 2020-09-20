first_list = [int(i) for i in input("Enter numbers separated by spaces and press Enter:").split()]
second_list = [int(j) for j in input("Enter numbers separated by spaces and press Enter:").split()]
same = ""
first_uniq = ""
second_uniq = ""
for k in range(len(first_list)):
    if first_list[k] in second_list:
        same += str(first_list[k]) + " "
    if first_list[k] not in second_list:
        first_uniq += str(first_list[k]) + " "
    if second_list[k] not in first_list:
        second_uniq += str(second_list[k]) + " "
print(same, first_uniq, first_uniq + second_uniq)