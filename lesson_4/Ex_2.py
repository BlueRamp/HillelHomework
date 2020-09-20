counter = 0
sum_of_numbers = 0
mult_of_numbers = 1
max_number = 0
count_odd_num = 0
while True:
    number = int(input("Input number:"))
    if number > 0 and number != 0:
        sum_of_numbers += number
        mult_of_numbers *= number
        counter += 1
        if max_number < number:
            second_max_number = max_number
            max_number = number
            max_number_index = counter - 1
            max_number_count = 0
        if max_number == number:
            max_number_count += 1
        if number % 2 > 0:
            count_odd_num += 1
    else:
        break
mean_of_numbers = sum_of_numbers/counter #Even if we have built-in function, i'm like Sinatra: did it my way =)
even_numbers = counter - count_odd_num
print("Quantity:", counter, "\nSum:", sum_of_numbers, "\nMultiplication:", mult_of_numbers, "\nMean", mean_of_numbers,
      "\nMax number:", max_number, "\nMax number index:", max_number_index,
       "\nEven numbers quantity:", even_numbers, "\nOdd numbers quantity:", count_odd_num,
      "\nSecond max number:", second_max_number, "\nQuantity of numbers equal to max:", max_number_count,)