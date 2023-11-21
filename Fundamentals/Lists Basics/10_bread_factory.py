events = input().split('|')
total_energy = 100
total_coins = 100
open_bakery = True

for event in events:
    event_name_or_ingredient, number = event.split('-')
    number = int(number)

    if event_name_or_ingredient == 'rest':
        current_energy = total_energy
        total_energy += number
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif event_name_or_ingredient == 'order':
        if total_energy >= 30:
            total_energy -= 30
            total_coins += number
            print(f"You earned {number} coins.")
        else:
            total_energy += 50
            print("You had to rest!")

    else:
        if total_coins >= number:
            total_coins -= number
            print(f"You bought {event_name_or_ingredient}.")
        else:
            print(f"Closed! Cannot afford {event_name_or_ingredient}." )
            open_bakery = False
            break

if open_bakery:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
