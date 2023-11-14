word = input()

my_list = [str(x) for x in str(word)]
empty_list = []
for current_string in range(len(my_list)):
    if my_list[current_string].isupper():
        empty_list.append(current_string)
print(empty_list)