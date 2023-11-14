word = input()
new_word = word.lower()

fish_count = new_word.count('fish')
water_count = new_word.count('water')
sun_count = new_word.count('sun')
sand_count = new_word.count('sand')

total = fish_count + water_count + sun_count + sand_count
print(total)