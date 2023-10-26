budget = float(input())
ticket_type = input()
number_of_people = int(input())
ticket_price = 0
transport = 0

if ticket_type == 'VIP':
    ticket_price = 499.99
elif ticket_type == 'Normal':
    ticket_price = 249.99

if 1 <= number_of_people <= 4:
    transport = budget * 0.75
elif 5 <= number_of_people <= 9:
    transport = budget * 0.6
elif 10 <= number_of_people <= 24:
    transport = budget * 0.5
elif 25 <= number_of_people <= 49:
    transport = budget * 0.4
elif 50 <= number_of_people:
    transport = budget * 0.25

total_tickets = ticket_price * number_of_people
money_left = budget - transport
if total_tickets >= money_left:
    print(f"Yes! You have {(total_tickets - money_left):.2f} leva left.")
else:
    print(f"Not enough money! You need {(money_left - total_tickets):.2f} leva.")
