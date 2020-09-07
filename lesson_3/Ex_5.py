import random
i = 0
x=random.randint(1,10)
while i != 3:
    number = int(input("input number from 1 to 10:"))
    if number >= 0 and number <= 10:
        if number == x:
            print("You Won!")
            i = 3
        else:
            print("You Lose! =(")
            i = i + 1
    else:
        print("Your number is not from 1 to 10")