a = int(input())
b = int(input())
max_number_of_passwords = int(input())
flag = False
counter_A = 0
counter_B = 0
counter_x = 0
counter_y = 0
passwords_counter = 0
passwords_countdown = max_number_of_passwords
while passwords_countdown > 0:
    if passwords_counter == a * b:
        break
    for x in range(1, a + 1):
        if passwords_counter == max_number_of_passwords:
            break
        for y in range(1, b + 1):
            if passwords_counter == max_number_of_passwords:
                break
            flag = False
            for A in range(35, 56):
                if A > 55:
                    A = 35
                if flag:
                    break
                A += counter_A

                for B in range(64, 97):
                    if B > 96:
                        B = 64
                    if flag:
                        break
                    B += counter_B

                    print(f'{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}', end='|')
                    passwords_countdown -= 1
                    passwords_counter += 1
                    flag = True
                    counter_A += 1
                    counter_B += 1
                    break
