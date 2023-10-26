start_of_interval = int(input())
end_of_interval = int(input())
magic_number = int(input())
counter = 0
flag = False

for x in range(start_of_interval, end_of_interval + 1):
    if flag:
        break
    for y in range(start_of_interval, end_of_interval + 1):
        result = x + y
        counter += 1
        if result == magic_number:
            print(f"Combination N:{counter} ({x} + {y} = {magic_number})")
            flag = True
            break
else:
    print(f"{counter} combinations - neither equals {magic_number}")