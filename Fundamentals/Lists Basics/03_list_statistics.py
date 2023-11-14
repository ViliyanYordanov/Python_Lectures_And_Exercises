n = int(input())

positive_list = []
negative_list = []

for _ in range(n):
    current_number = int(input())

    if current_number >= 0:
        positive_list.append(current_number)
    else:
        negative_list.append(current_number)

print(positive_list)
print(negative_list)
positive_list_count = len(positive_list)
negative_list_sum = sum(negative_list)
print(f"Count of positives: {positive_list_count}")
print(f"Sum of negatives: {negative_list_sum}")