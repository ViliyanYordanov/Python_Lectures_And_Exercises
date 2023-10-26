last_sector = input()
first_sector_rows = int(input())
odd_row_seats = int(input())
flag = False
counter = 0

for sector in range(65, ord(last_sector) + 1):
    if flag:
        first_sector_rows += 1
    flag = True
    for rows in range(1, first_sector_rows + 1):
        if rows % 2 == 0:
            for seats_even in range(97, odd_row_seats + 99):
                print(f'{chr(sector)}{rows}{chr(seats_even)}')
                counter += 1
        else:
            for seats_odd in range(97, odd_row_seats + 97):
                print(f'{chr(sector)}{rows}{chr(seats_odd)}')
                counter += 1
print(counter)

