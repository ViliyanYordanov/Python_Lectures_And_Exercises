movie_budget = float(input())
number_employees = int(input())
outfit_money_per_employee = float(input())

decor = movie_budget * 0.1
total_outfit_money = number_employees * outfit_money_per_employee

if number_employees > 150:
    total_outfit_money = total_outfit_money * 0.9

cost = total_outfit_money + decor

if cost > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(cost - movie_budget):.2f} leva more.")
elif cost <= movie_budget:
    print("Action!")
    print(f"Wingard starts filming with {abs(cost - movie_budget):.2f} leva left.")
