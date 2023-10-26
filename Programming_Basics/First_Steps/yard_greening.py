square_metres_yard = float(input())

price_for_yard_greening = square_metres_yard * 7.61
discount_price = price_for_yard_greening * 0.18
final_price = price_for_yard_greening - discount_price

print(f'The final price is: {final_price} lv.')
print(f'The discount is: {discount_price} lv.')