
name_of_company = input()
elderly_tickets = int(input())
children_tickets = int(input())
elderly_tickets_price = float(input())
tax = float(input())
children_tickets_price = elderly_tickets_price * 0.3 + tax
elderly_tickets_price += tax

elderly_money = elderly_tickets * elderly_tickets_price
children_money =children_tickets * children_tickets_price
total_money = elderly_money + children_money

profit = total_money * 0.2

print(f"The profit of your agency from {name_of_company} tickets is {profit:.2f} lv.")

