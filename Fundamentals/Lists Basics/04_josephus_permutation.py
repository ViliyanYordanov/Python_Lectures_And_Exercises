persons = input().split()
persons.reverse()
k = int(input())
total_persons = len(persons)
executed_list = []

while total_persons != 0:
    for person in range(len(persons) - k, -1, - k):
        executed_list.append(persons[person])
        persons.pop(person)
        total_persons -= 1
        print(executed_list)
