position_one = [int(input("Input current coordinate x:")), int(input("Input current coordinate x:"))]
position_two = [int(input("Input further coordinate x:")), int(input("Input further coordinate x:"))]
if 0 < abs(position_one[0]-position_two[0]) <= 2 and 0 < abs(position_one[1]-position_two[1]) <= 2 and abs(position_one[0]-position_two[0]) != abs(position_one[1]-position_two[1]):
    print("Yes")
else:
    print("No")
