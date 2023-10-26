CONSTANT_NUMBER = int(input())
total = 0

# while True:
#     current_num = int(input())
#     total += current_num
#
#     if total >= CONSTANT_NUMBER:
#         print(total)
#         break


while total < CONSTANT_NUMBER:
    current_num = int(input())
    total += current_num
else:
    print(total)