nylon = int(input())
paint = int(input())
diluent = int(input())
hours = int(input())

nylon_price = (nylon + 2) * 1.50
paint_price = (paint + paint * 10 / 100) * 14.50
diluent_price = diluent * 5.00

whole_amount = nylon_price + paint_price + diluent_price + 0.40
payroll = whole_amount * 30 / 100 * hours

print(whole_amount + payroll)
