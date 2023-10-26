hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())
condition = ''
exam_time = hour_of_exam * 60 + minute_of_exam  # exam time in minutes
arrival_time = hour_of_arrival * 60 + minute_of_arrival  # arrival time in minutes
diff = exam_time - arrival_time
time = ''
if arrival_time > exam_time:
    condition = 'Late'
elif 0 <= diff <= 30:
    condition = 'On time'
elif diff > 30:
    condition = 'Early'
if 0 < diff < 60:
    time = f'{abs(diff)} minutes before the start'
elif diff >= 60:
    time = f'{abs(diff)//60}:{abs(diff)%60:02} hours before the start'
if 0 > diff > -60:
    time = f'{abs(diff)} minutes after the start'
elif diff <= -60:
    time = f'{abs(diff)//60}:{abs(diff)%60:02} hours after the start'
print(condition)
print(time)
