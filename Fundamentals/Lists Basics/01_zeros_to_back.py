data = input().split(', ')
popped_elements = []

for element in range(len(data) -1, -1, -1):
    if data[element] == '0':
        popped_elements.append(int(data[element]))
        data.pop(element)
for x in popped_elements:
    data.insert(len(data), str(x))

data_int = []
for y in data:
    data_int.append(int(y))
print(data_int)