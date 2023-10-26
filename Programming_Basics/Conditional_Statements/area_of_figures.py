from math import pi
figure = str(input())
area = 0

if figure == 'square':
    a = float(input())
    area = a**2
    print(f'{area:.3f}')
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
    print(f'{area:.3f}')
elif figure == 'circle':
    r = float(input())
    area = pi * r**2
    print(f'{area:.3f}')
elif figure == 'triangle':
    a = float(input())
    h = float(input())
    area = a * h / 2
    print(f'{area:.3f}')
