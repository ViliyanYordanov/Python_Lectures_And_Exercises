number_of_joinery = int(input())
type_of_joinery = input()
delivery = input()
price_per_one = 0
flag = False

while number_of_joinery > 10:

    if type_of_joinery == '90X130':
        price_per_one = 110
        if 30 < number_of_joinery <= 60:
            price_per_one *= 0.95
        elif number_of_joinery > 60:
            price_per_one *= 0.92

    elif type_of_joinery == '100X150':
        price_per_one = 140
        if 40 < number_of_joinery <= 80:
            price_per_one *= 0.94
        elif number_of_joinery > 80:
            price_per_one *= 0.9

    elif type_of_joinery == '130X180':
        price_per_one = 190
        if 20 < number_of_joinery <= 50:
            price_per_one *= 0.93
        elif number_of_joinery > 50:
            price_per_one *= 0.88

    elif type_of_joinery == '200X300':
        price_per_one = 250
        if 25 < number_of_joinery <= 50:
            price_per_one *= 0.91
        elif number_of_joinery > 50:
            price_per_one *= 0.86

    total_price = price_per_one * number_of_joinery
    if delivery == 'With delivery':
        total_price += 60
    if number_of_joinery > 99:
        total_price *= 0.96
    flag = True
    break
else:
    print("Invalid order")

if flag:
    print(f"{total_price:.2f} BGN")
