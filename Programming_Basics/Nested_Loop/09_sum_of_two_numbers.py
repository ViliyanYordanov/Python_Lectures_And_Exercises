start = int(input())
end = int(input())
magic_number = int(input())
counter = 0
flag = False

for a in range(start, end + 1):
    if flag:
        break
    for b in range(start, end + 1):
        x = a + b
        counter += 1
        if x == magic_number:
            print(f"Combination N:{counter} ({a} + {b} = {x})")
            flag = True
            break
if x != magic_number:
    print(f"{counter} combinations - neither equals {magic_number}")
