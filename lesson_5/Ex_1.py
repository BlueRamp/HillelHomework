try_again = "Yes"
while try_again == "Yes":
    try:
        number = int(input("Input prime number:"))
    except ValueError as error:
        print(error)


    def is_prime(number):
        i = 2
        j = 0
        while True:
            if i * i <= number and j != 1:
                if number % i == 0:
                    j = 1
                    i += 1
                else:
                    i += 1
            else:
                if j == 1:
                    return "Not prime number"
                if number == 1:
                    return "Seems like smart guys didn't decide is 1 prime number or not"
                else:
                    return "Prime number"
    if number > 0:
        print(is_prime(number))
        try_again = input("if you want to try again, input \"Yes\":").capitalize()
    else:
        print("Please don't input negative numbers")
        try_again = input("if you want to try again, input \"Yes\":").capitalize()
