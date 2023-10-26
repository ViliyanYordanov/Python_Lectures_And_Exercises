group_budget = int(input())
season = input()
fishermen = int(input())
boat_rent = 0

if season == 'Spring':
    boat_rent = 3000
    if fishermen <= 6:
        boat_rent = boat_rent * 0.9
    elif 7 <= fishermen <= 11:
        boat_rent = boat_rent * 0.85
    elif fishermen >= 12:
        boat_rent = boat_rent * 0.75
    if fishermen % 2 == 0:
        boat_rent = boat_rent * 0.95

elif season == 'Summer':
    boat_rent = 4200
    if fishermen <= 6:
        boat_rent = boat_rent * 0.9
    elif 7 <= fishermen <= 11:
        boat_rent = boat_rent * 0.85
    elif fishermen >= 12:
        boat_rent = boat_rent * 0.75
    if fishermen % 2 == 0:
        boat_rent = boat_rent * 0.95
elif season == 'Autumn':
    boat_rent = 4200
    if fishermen <= 6:
        boat_rent = boat_rent * 0.9
    elif 7 <= fishermen <= 11:
        boat_rent = boat_rent * 0.85
    elif fishermen >= 12:
        boat_rent = boat_rent * 0.75
elif season == 'Winter':
    boat_rent = 2600
    if fishermen <= 6:
        boat_rent = boat_rent * 0.9
    elif 7 <= fishermen <= 11:
        boat_rent = boat_rent * 0.85
    elif fishermen >= 12:
        boat_rent = boat_rent * 0.75
    if fishermen % 2 == 0:
        boat_rent = boat_rent * 0.95

if group_budget >= boat_rent:
    print(f"Yes! You have {(group_budget - boat_rent):.2f} leva left.")
else:
    print(f"Not enough money! You need {(boat_rent - group_budget):.2f} leva.")
