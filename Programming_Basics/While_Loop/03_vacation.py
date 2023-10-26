trip_money = float(input())
current_money = float(input())
spend_counter = 0
days = 0

while True:
    action = input()
    amount = float(input())
    days += 1
    if action == 'spend':
        spend_counter += 1
        current_money -= amount
        if current_money < 0:
            current_money = 0
    elif action == 'save':
        spend_counter = 0
        current_money += amount
    if spend_counter == 5:
        print("You can't save the money.")
        print(f"{days}")
        break

    if current_money >= trip_money:
        print(f"You saved the money for {days} days.")
        break