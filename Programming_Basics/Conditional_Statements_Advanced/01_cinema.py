projection = input()
rows = int(input())
columns = int(input())
tickets_amount = rows * columns
price = 0

if projection == 'Premiere':
    price = tickets_amount * 12
elif projection == 'Normal':
    price = tickets_amount * 7.5
elif projection == 'Discount':
    price = tickets_amount * 5

print(f'{price:.2f} leva')