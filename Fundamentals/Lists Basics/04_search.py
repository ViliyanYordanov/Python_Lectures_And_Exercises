n = int(input())
word = input()
my_list = []
for _ in range(n):
    current_string = input()
    my_list.append(current_string)
print(my_list)

for x in range(len(my_list) - 1, -1, -1):
    if word not in my_list[x]:
        my_list.remove(my_list[x])
print(my_list)
