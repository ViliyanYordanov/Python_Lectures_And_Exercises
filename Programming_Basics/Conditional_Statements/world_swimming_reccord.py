record_in_seconds = float(input())
distance_in_metres = float(input())
seconds_per_metre = float(input())

resistance = distance_in_metres // 15
ivan_time = distance_in_metres * seconds_per_metre + resistance * 12.5

if ivan_time < record_in_seconds:
    print(f" Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(record_in_seconds-ivan_time):.2f} seconds slower.")
