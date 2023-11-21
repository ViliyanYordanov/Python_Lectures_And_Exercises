# items_for_sale = input().split('|')
# budget = float(input())
# clothes_max_price = 50.00
# shoes_max_price = 35.00
# accessories_max_price = 20.50
# train_ticket = 150
# profit = 0
# new_prices_list = []
# sum_of_all_new_prices = 0
#
# for current_item in range(len(items_for_sale)):
#     if budget <= 0:
#         break
#     items_list = items_for_sale[current_item].split('->')
#     if items_list[0] == 'Clothes' and float(items_list[1]) <= clothes_max_price:
#         item_price = float(items_list[1])
#         if budget >= item_price:
#             budget -= item_price
#             item_new_price = round(item_price * 1.4, 2)
#             profit += item_new_price - item_price
#             new_prices_list.append(str(item_new_price))
#             sum_of_all_new_prices += item_new_price
#         else:
#             continue
#     elif items_list[0] == 'Shoes' and float(items_list[1]) <= shoes_max_price:
#         item_price = float(items_list[1])
#         if budget >= item_price:
#             budget -= item_price
#             item_new_price = round(item_price * 1.4, 2)
#             profit += item_new_price - item_price
#             new_prices_list.append(str(item_new_price))
#             sum_of_all_new_prices += item_new_price
#         else:
#             continue
#     elif items_list[0] == 'Accessories' and float(items_list[1]) <= accessories_max_price:
#         item_price = float(items_list[1])
#         if budget >= item_price:
#             budget -= item_price
#             item_new_price = round(item_price * 1.4, 2)
#             profit += item_new_price - item_price
#             new_prices_list.append(str(item_new_price))
#             sum_of_all_new_prices += item_new_price
#         else:
#             continue
#
#
# print(' '.join(new_prices_list))
# print(f"Profit: {profit:.2f}")
# if budget + sum_of_all_new_prices >= train_ticket:
#     print("Hello, France!")
# else:
#     print("Not enough money.")


items = input().split('|')
budget = int(input())
clothes_max_price = 50.00
shoes_max_price = 35.00
accessories_max_price = 20.50
ticket_price = 150

for item in items:
    items_list = item.split('->')
    current_item = items_list[0]
    price = float(items_list[1])


