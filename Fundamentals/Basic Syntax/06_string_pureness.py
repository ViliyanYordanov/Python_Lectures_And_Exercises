n = int(input())

for _ in range(n):
    string = input()
    for i in range(len(string)):
        if string[i] == '_' or string[i] == '.' or string[i] == ',':
            print(f"{string} is not pure!")
            break
    else:
        print(f"{string} is pure.")

# n = int(input())
#
# for _ in range(n):
#     current_string = input()
#
#     if ',' not in current_string and '.' not in current_string and '_' not in current_string:
#         print(f"{current_string} is pure.")
#     else:
#         print(f"{current_string} is not pure!")

