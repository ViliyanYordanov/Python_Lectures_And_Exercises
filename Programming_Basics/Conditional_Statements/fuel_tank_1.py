fuel_type = str(input())
fuel_litres = float(input())

if fuel_litres >= 25 and fuel_type == 'Diesel':
    print('You have enough gasoline.')
elif fuel_litres >= 25 and fuel_type == 'Gasoline':
    print('You have enough gasoline.')
elif fuel_litres >= 25 and fuel_type == 'Gas':
    print('You have enough gasoline.')
elif fuel_litres < 25 and fuel_type == 'Diesel':
    print(f"Fill your tank with {fuel_type}!")
elif fuel_litres < 25 and fuel_type == 'Gasoline':
    print(f"Fill your tank with {fuel_type}!")
elif fuel_litres < 25 and fuel_type == 'Gas':
    print(f"Fill your tank with {fuel_type}!")
else:
    print("Invalid fuel!")
