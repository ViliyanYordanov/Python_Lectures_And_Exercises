vegetable_kg_price_lv = float(input())
fruit_kg_price_lv = float(input())
total_kg_vegetable = int(input())
total_kg_fruit = int(input())

# vegetable_euro = vegetable_kg_price_lv * 1.94
# fruit_euro = fruit_kg_price_lv * 1.94

income = vegetable_kg_price_lv * total_kg_vegetable + fruit_kg_price_lv * total_kg_fruit
income_euro = income / 1.94
print("{:.2f}".format(income_euro))


