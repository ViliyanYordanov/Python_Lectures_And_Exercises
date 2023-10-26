initial_first_pair = int(input())
initial_second_pair = int(input())
difference_first_pair = int(input())
difference_second_pair = int(input())

end_first_pair = initial_first_pair + difference_first_pair
end_second_pair = initial_second_pair + difference_second_pair
first_pair_counter = 0
second_pair_counter = 0

for a in range(initial_first_pair, end_first_pair + 1):
    for b in range(initial_second_pair, end_second_pair + 1):
        for x in range(1, a + 1):
            if a % x == 0:
                first_pair_counter += 1
        for y in range(1, b + 1):
            if b % y == 0:
                second_pair_counter += 1
        if first_pair_counter == 2 and second_pair_counter == 2:
            print(f'{a}{b}')
        else:
            first_pair_counter = 0
            second_pair_counter = 0

