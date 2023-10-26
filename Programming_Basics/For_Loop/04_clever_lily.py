n = int(input())
washing_machine = float(input())
toy_price = int(input())
money = 0
toys = 0

for current_age in range(1, n + 1):
    # current_age = int(input())
    if current_age % 2 == 0:
        money += (10 * (current_age / 2)) - 1
    else:
        toys += 1
toys_money = toys * toy_price
all_money = toys_money + money

if all_money >= washing_machine:
    print(f"Yes! {(all_money - washing_machine):.2f}")
else:
    print(f"No! {(washing_machine - all_money):.2f}")
