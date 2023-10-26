first_number = int(input())
second_number = int(input())
third_number = int(input())

for a in range(2, first_number + 1, 2):
    for b in range(2, second_number + 1):
        prime_numbers = 0
        for delitel in range(1, second_number + 1):
            if b % delitel == 0:
                prime_numbers += 1
        if prime_numbers < 3:
            for c in range(2, third_number + 1, 2):
                print(a, b, c, )
