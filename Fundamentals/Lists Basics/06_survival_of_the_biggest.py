list_of_integer = input().split()
n = int(input())
numbers_list = []

for x in range(len(list_of_integer)):
    numbers_list.append(int(list_of_integer[x]))
numbers_list.sort()

for i in range(n):
    list_of_integer.remove(str(numbers_list[i]))

list_of_integer = ', '.join(list_of_integer)
print(list_of_integer)

