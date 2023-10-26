first_number = int(input())
second_number = int(input())

for i in range(first_number, second_number + 1):
    current_num_str = str(i)

    current_number_odd_1 = int(current_num_str[0])
    current_number_odd_3 = int(current_num_str[2])
    current_number_odd_5 = int(current_num_str[4])
    current_number_even_2 = int(current_num_str[1])
    current_number_even_4 = int(current_num_str[3])
    current_number_even_6 = int(current_num_str[5])

    odd_sum = current_number_odd_1 + current_number_odd_3 + current_number_odd_5
    even_sum = current_number_even_2 + current_number_even_4 + current_number_even_6

    if odd_sum == even_sum:
        print(current_num_str, end=' ')