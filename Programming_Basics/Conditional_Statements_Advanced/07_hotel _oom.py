month = input()
overnight_stays = int(input())
apartment = 0
studio = 0

if month == 'May' or month == 'October':
    if overnight_stays <= 7:
        studio = overnight_stays * 50
    elif 7 < overnight_stays <= 14:
        studio = overnight_stays * 50 * 0.95
    elif overnight_stays > 14:
        studio = overnight_stays * 50 * 0.7
    if overnight_stays <= 14:
        apartment = overnight_stays * 65
    else:
        apartment = overnight_stays * 65 * 0.9
elif month == 'June' or month == 'September':
    if overnight_stays <= 14:
        studio = overnight_stays * 75.2
    else:
        studio = overnight_stays * 75.2 * 0.8
    if overnight_stays <= 14:
        apartment = overnight_stays * 68.7
    else:
        apartment = overnight_stays * 68.7 * 0.9
elif month == 'July' or month == 'August':
    studio = overnight_stays * 76
    if overnight_stays <= 14:
        apartment = overnight_stays * 77
    else:
        apartment = overnight_stays * 77 * 0.9

print(f'Apartment: {apartment:.2f} lv.')
print(f'Studio: {studio:.2f} lv.')


# month = input()
# count_nights = int(input())
#
# studio_price = 0
# apartment_price = 0
#
# if month == 'May' or month == 'October':
#     studio_price = 50 * count_nights
#     apartment_price = 65 * count_nights
# elif month == 'June' or month == 'September':
#     studio_price = 75.2 * count_nights
#     apartment_price = 68.7 * count_nights
# elif month == 'July' or month == 'August':
#     studio_price = 76 * count_nights
#     apartment_price = 77 * count_nights
#
# if count_nights > 14 and (month == 'May' or month == 'October'):
#     studio_price = studio_price * 0.7
# elif count_nights > 7 and (month == 'May' or month == 'October'):
#     studio_price = studio_price * 0.95
# elif count_nights > 14 and (month == 'June' or month == 'September'):
#     studio_price = studio_price * 0.8
#
# if count_nights > 14:
#     apartment_price = apartment_price * 0.9
#
# print(f'Apartment: {apartment_price:.2f} lv.')
# print(f'Studio: {studio_price:.2f} lv.')
