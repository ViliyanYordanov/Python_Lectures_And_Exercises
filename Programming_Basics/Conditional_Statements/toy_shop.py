trip_price = float(input())
number_puzzle = int(input())
number_doll = int(input())
number_teddy_bear = int(input())
number_minion = int(input())
number_truck = int(input())

total_toys = number_minion + number_truck + number_doll + number_puzzle + number_teddy_bear
price_puzzle = number_puzzle * 2.60
price_doll = number_doll * 3
price_teddy_bear = number_teddy_bear * 4.10
price_minion = number_minion * 8.20
price_truck = number_truck * 2
total_price = price_truck + price_minion + price_doll + price_puzzle + price_teddy_bear

if total_toys >= 50:
    total_price = total_price * 0.75

rent = total_price * 0.10

money_left = total_price - rent

if money_left >= trip_price:
    money_left = money_left - trip_price
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_left = money_left - trip_price
    print(f"Not enough money! {abs(money_left):.2f} lv needed.")
