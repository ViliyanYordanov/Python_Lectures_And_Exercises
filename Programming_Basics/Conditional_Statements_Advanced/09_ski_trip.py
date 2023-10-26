count_days = int(input())
premise = input()
evaluation = input()

count_days = count_days - 1
room_for_one_person_price = 18 * count_days
apartment_price = 25 * count_days
president_apartment_price = 35 * count_days

total = 0

if count_days < 10:
    if premise == 'room for one person':
        total = room_for_one_person_price
    elif premise == 'apartment':
        total = apartment_price * 0.7
    elif premise == 'president apartment':
        total = apartment_price * 0.9
elif 10 <= count_days <= 15:
    if premise == 'room for one person':
        total = room_for_one_person_price
    elif premise == 'apartment':
        total = apartment_price * 0.65
    elif premise == 'president apartment':
        total = apartment_price * 0.85
elif count_days > 15:
    if premise == 'room for one person':
        total = room_for_one_person_price
    elif premise == 'apartment':
        total = apartment_price * 0.5
    elif premise == 'president apartment':
        total = president_apartment_price * 0.8

if evaluation == 'positive':
    total = total + total * 0.25
elif evaluation == 'negative':
    total = total - total * 0.1
print(f'{total:.2f}')
