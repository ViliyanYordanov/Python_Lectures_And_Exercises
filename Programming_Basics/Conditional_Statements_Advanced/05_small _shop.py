product = input()
city = input()
amount = float(input())

if city == 'Sofia':
    if product == 'coffee':
        print(amount * 0.50)
    elif product == 'water':
        print(amount * 0.80)
    elif product == 'beer':
        print(amount * 1.20)
    elif product == 'sweets':
        print(amount * 1.45)
    elif product == 'peanuts':
        print(amount * 1.60)
elif city == 'Plovdiv':
    if product == 'coffee':
        print(amount * 0.40)
    elif product == 'water':
        print(amount * 0.70)
    elif product == 'beer':
        print(amount * 1.15)
    elif product == 'sweets':
        print(amount * 1.30)
    elif product == 'peanuts':
        print(amount * 1.50)
elif city == 'Varna':
    if product == 'coffee':
        print(amount * 0.45)
    elif product == 'water':
        print(amount * 0.70)
    elif product == 'beer':
        print(amount * 1.10)
    elif product == 'sweets':
        print(amount * 1.35)
    elif product == 'peanuts':
        print(amount * 1.55)
