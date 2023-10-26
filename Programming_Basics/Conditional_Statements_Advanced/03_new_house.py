flower_type = input()
flower_amount = int(input())
budget = int(input())
price = 0

if flower_type == 'Roses':
    if flower_amount > 80:
        price = flower_amount * 0.9 * 5
    else:
        price = flower_amount * 5
elif flower_type == 'Dahlias':
    if flower_amount > 90:
        price = flower_amount * 0.85 * 3.8
    else:
        price = flower_amount * 3.8
elif flower_type == 'Tulips':
    if flower_amount > 80:
        price = flower_amount * 0.85 * 2.8
    else:
        price = flower_amount * 2.8
elif flower_type == 'Narcissus':
    if flower_amount < 120:
        price = flower_amount * 1.15 * 3
    else:
        price = flower_amount * 3
elif flower_type == 'Gladiolus':
    if flower_amount < 80:
        price = flower_amount * 1.2 * 2.5
    else:
        price = flower_amount * 2.5

if budget >= price:
    print(f"Hey, you have a great garden with {flower_amount} {flower_type} and {(budget - price):.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(budget - price):.2f} leva more.")