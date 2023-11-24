def calculations(operator: str, first_num: int, second_num: int):
    if operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return int(a / b)
    elif operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b


operation = input()
a = int(input())
b = int(input())

print(calculations(operation, a, b))
