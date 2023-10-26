a = int(input())
b = int(input())
max_number_of_passwords = int(input())

total_pass = max_number_of_passwords
A = 35
B = 64
A_counter = 0
B_counter = 0
prints_counter = 0

for x in range(1, a + 1):
    if total_pass == 0 or prints_counter == a * b:
        break
    for y in range(1, b + 1):
        flag = False
        while A < 56:
            if flag:
                break
            while B < 97:
                if flag:
                    break
                A += A_counter
                B += B_counter
                print(f'{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}', end='|')
                prints_counter += 1
                if prints_counter == a * b:
                    flag = True
                    break
                A_counter = 1
                B_counter = 1
                total_pass -= 1
                if total_pass == 0:
                    flag = True
                    break
                flag = True
                break
            else:
                B = 64
                break
        else:
            A = 35
            break
