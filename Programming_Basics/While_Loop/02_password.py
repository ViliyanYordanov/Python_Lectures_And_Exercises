# username = input()
# password = input()
#
# while True:
#     current_password = input()
#
#     if current_password != password:
#         continue
#     else:
#         print(f"Welcome {username}!")
#         break
#

username = input()
password = input()
current_password = input()

while password != current_password:
    current_password = input()
    continue
else:
    print(f"Welcome {username}!")
    # break