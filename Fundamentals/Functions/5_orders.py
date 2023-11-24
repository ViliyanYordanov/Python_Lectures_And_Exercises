coffee_price = 1.50
water_price = 1.00
coke_price = 1.40
snacks_price = 2.00


def price_calculator(product, quantity):
    if current_product == 'coffee':
        return current_quantity * coffee_price
    elif current_product == 'water':
        return current_quantity * water_price
    elif current_product == 'coke':
        return current_quantity * coke_price
    elif current_product == 'snacks':
        return current_quantity * snacks_price


current_product = input()
current_quantity = int(input())
print(f'{price_calculator(current_product, current_quantity):.2f}')
