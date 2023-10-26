a = int(input())
b = int(input())
max_pass = int(input())

A = 35
B = 64
counter_A = 0
counter_B = 0
pass_counter = 0
pass_flag = False

for x in range(1, a + 1):
    if pass_flag:
        break
    for y in range(1, b + 1):
        if pass_flag:
            break
        flag = False
        while A < 56:
            if flag:
                break
            A += counter_A
            while B < 96:
                B += counter_B
                if pass_counter == max_pass:
                    pass_flag = True
                    flag = True
                    break
                if A > 56:
                    A = 35
                if B > 96:
                    B = 64
                print(f'{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}', end='|')
                pass_counter += 1
                counter_A = 1
                counter_B = 1
                flag = True
                break

