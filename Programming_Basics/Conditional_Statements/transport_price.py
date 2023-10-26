n_km = float(input())
day_night = str(input())

taxi_enter = 0.70
taxi_day_per_km = 0.79
taxi_night_per_km = 0.90
bus_per_km = 0.09
train_per_km = 0.06

trip_price = 0

if n_km >= 100:
    trip_price = n_km * train_per_km
    print(f'{trip_price:.2f}')
elif 20 <= n_km < 100:
    trip_price = n_km * bus_per_km
    print(f'{trip_price:.2f}')
elif n_km < 20 and day_night == 'day':
    trip_price = taxi_enter + taxi_day_per_km * n_km
    print(f'{trip_price:.2f}')
elif n_km < 20 and day_night == 'night':
    trip_price = taxi_enter + taxi_night_per_km * n_km
    print(f'{trip_price:.2f}')
