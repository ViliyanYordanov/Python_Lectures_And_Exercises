chicken_menu = int(input())
fish_menu = int(input())
veg_menu = int(input())

chicken_menu_price = chicken_menu * 10.35
fish_menu_price = fish_menu * 12.40
veg_menu_price = veg_menu * 8.15
desert = (chicken_menu_price + fish_menu_price + veg_menu_price) * 20 / 100

total_price = chicken_menu_price + fish_menu_price + veg_menu_price + desert + 2.50
print(total_price)
