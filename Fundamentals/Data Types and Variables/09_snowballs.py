number_of_snowballs = int(input())
max_value = 0
max_value_weight = 0
max_value_time = 0
max_value_quality = 0

for current_snowball in range(number_of_snowballs):
    last_value = max_value
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    value = (snowball_weight / snowball_time) ** snowball_quality
    if value > last_value:
        max_value = value
        max_value_weight = snowball_weight
        max_value_time = snowball_time
        max_value_quality = snowball_quality

print(f"{max_value_weight} : {max_value_time} = {int(max_value)} ({max_value_quality})")
