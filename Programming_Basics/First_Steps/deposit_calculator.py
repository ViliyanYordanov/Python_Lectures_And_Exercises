deposit = float(input())
deposit_period = int(input())
interest_rate = float(input())

total = deposit + deposit_period * (deposit * (interest_rate/100)/12)

print(total)
