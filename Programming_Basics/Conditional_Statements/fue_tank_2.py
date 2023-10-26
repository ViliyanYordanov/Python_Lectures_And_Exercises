fuel_type = str(input())
fuel_litres = float(input())
discount_card = str(input())

gasoline_price = fuel_litres * 2.22
diesel_price = fuel_litres * 2.33
gas_price = fuel_litres * 0.93

gasoline_price_card = fuel_litres * (2.22 - 0.18)
diesel_price_card = fuel_litres * (2.33 - 0.12)
gas_price_card = fuel_litres * (0.93 - 0.08)
bill = 0

if discount_card == 'Yes' and fuel_type == 'Gasoline':
    bill = gasoline_price_card
if discount_card == 'Yes' and fuel_type == 'Diesel':
    bill = diesel_price_card
if discount_card == 'Yes' and fuel_type == 'Gas':
    bill = gas_price_card

if discount_card == 'No' and fuel_type == 'Gasoline':
    bill = gasoline_price
if discount_card == 'No' and fuel_type == 'Diesel':
    bill = diesel_price
if discount_card == 'No' and fuel_type == 'Gas':
    bill = gas_price

if fuel_litres < 20:
    print(f'{(bill):.2f} lv.')
if 20 <= fuel_litres <= 25:
    print(f'{(bill * 0.92):.2f} lv.')
elif fuel_litres > 25:
    print(f'{(bill * 0.90):.2f} lv.')
