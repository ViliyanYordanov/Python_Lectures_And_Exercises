budget = int(input())

while True:
    price = input()
    if price == 'End':
        break
    price = int(price)
    budget -= price
    if budget < 0:
        print("You went in overdraft!")
        break
if budget >= 0:
    print('You bought everything needed.')
