budget = float(input())
flour_price_1kg = float(input())
eggs_price_1pack = flour_price_1kg * 0.75
milk_price_1l = flour_price_1kg * 1.25

bread_cost = flour_price_1kg + eggs_price_1pack + (milk_price_1l / 4)
bread_counter = 0
eggs_counter = 0

while budget >= bread_cost:
    budget -= bread_cost
    bread_counter += 1
    eggs_counter += 3

    if bread_counter % 3 == 0:
        eggs_counter -= (bread_counter - 2)

print(f"You made {bread_counter} loaves of Easter bread! Now you have {eggs_counter} eggs and {budget:.2f}BGN left.")
