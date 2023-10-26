coffees = 0

while True:
    command = input()
    if command == 'END':
        break

    if command == 'coding' or command == 'dog' or command == 'cat' or command == 'movie':
        coffees += 1
    elif command == 'CODING' or command == 'DOG' or command == 'CAT' or command == 'MOVIE':
        coffees += 2
    else:
        continue
if coffees <= 5:
    print(coffees)
else:
    print('You need extra sleep')
