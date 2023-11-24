def grade(n):
    current_grade = ''
    if 2.00 <= n <= 2.99:
        current_grade = 'Fail'
    elif 3.00 <= n <= 3.49:
        current_grade = 'Poor'
    elif 3.50 <= n <= 4.49:
        current_grade = 'Good'
    elif 4.50 <= n <= 5.49:
        current_grade = 'Very Good'
    elif 5.50 <= n <= 6.00:
        current_grade = 'Excellent'

    return current_grade


print(grade(float(input())))
