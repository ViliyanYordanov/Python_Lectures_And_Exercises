from math import ceil
series = str(input())
episode_time = int(input())
break_time = int(input())

lunch_time = break_time / 8
relax_time = break_time / 4
break_time_left = break_time - lunch_time - relax_time

if break_time_left >= episode_time:
    print(f"You have enough time to watch {series} and left with {ceil(break_time_left - episode_time)} "
          f"minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {ceil(episode_time - break_time_left)} more minutes.")
