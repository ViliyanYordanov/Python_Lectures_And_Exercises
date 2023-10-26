n1 = int(input())
n2 = int(input())
symbol = input()
total = 0
even_odd = ''
divide_0 = False

if symbol == '+':
    total = n1 + n2
    if total % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
elif symbol == '-':
    total = n1 - n2
    if total % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
elif symbol == '*':
    total = n1 * n2
    if total % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
elif symbol == '/':
    if n2 != 0:
        total = n1 / n2
    else:
        divide_0 = True
elif symbol == '%':
    if n2 != 0:
        total = n1 % n2
    else:
        divide_0 = True

if divide_0:
    print(f'Cannot divide {n1} by zero')
elif divide_0 is False and symbol == '/':
    print(f'{n1} / {n2} = {total:.2f}')
elif divide_0 is False and symbol == '%':
    print(f'{n1} % {n2} = {total}')
else:
    print(f'{n1} {symbol} {n2} = {total} - {even_odd}')
