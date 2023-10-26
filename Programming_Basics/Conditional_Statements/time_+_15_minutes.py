hour = int(input())
minutes = int(input())

time = hour * 60 + minutes
new_time = time + 15
hour_new = new_time // 60
minutes_new = new_time % 60

if hour_new >= 24:
    hour_new = hour_new - 24
if 0 <= minutes_new < 10:
    minutes_new = f'0{minutes_new}'

print(f'{hour_new}:{minutes_new}')
