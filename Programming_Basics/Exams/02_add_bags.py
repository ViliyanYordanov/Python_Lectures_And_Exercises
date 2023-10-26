price_over_20kg = float(input())
luggage_kg = float(input())
days_until_trip = int(input())
number_of_luggage = int(input())
price = 0

if luggage_kg <= 10:
    price = price_over_20kg * 0.2
elif 10 < luggage_kg <= 20:
    price = price_over_20kg * 0.5
else:
    price = price_over_20kg
total_price = price * number_of_luggage

if days_until_trip > 30:
    total_price *= 1.1
elif 7 <= days_until_trip <= 30:
    total_price *= 1.15
else:
    total_price *= 1.4

print(f"The total price of bags is: {total_price:.2f} lv. ")