number_of_lines = int(input())
open_brackets_flag = False
closed_brackets_flag = False

for _ in range(number_of_lines):
    line = input()

    if line == '(':
        if open_brackets_flag:
            print('UNBALANCED')
            break
        else:
            open_brackets_flag = True
    if line == ')':
        if closed_brackets_flag or not open_brackets_flag:
            print('UNBALANCED')
            break
        else:
            closed_brackets_flag = True
    if open_brackets_flag and closed_brackets_flag:
        open_brackets_flag = False
        closed_brackets_flag = False
else:
    print('BALANCED')