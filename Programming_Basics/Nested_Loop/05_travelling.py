while True:
    country = input()
    if country == 'End':
        break
    budget = float(input())
    while True:
        savings = float(input())
        budget -= savings

        if budget <= 0:
            print(f"Going to {country}!")
            break