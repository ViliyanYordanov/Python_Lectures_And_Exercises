vacation_days = int(input())

working_time_play = (365 - vacation_days) * 63
resting_time_play = vacation_days * 127
total_play = working_time_play + resting_time_play

if total_play >= 30000:
    print('Tom will run away')
    print(f'{abs(30000 - total_play) // 60} hours and {abs(30000 - total_play) % 60} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{abs(30000 - total_play) // 60} hours and {abs(30000 - total_play) % 60} minutes less for play')
