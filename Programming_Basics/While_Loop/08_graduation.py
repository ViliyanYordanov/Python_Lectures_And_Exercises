name = input()
failed_years = 0
total_grade_score = 0
grade = 0

while True:
    current_grade = float(input())

    if current_grade < 4:
        failed_years += 1
    else:
        total_grade_score += current_grade
        grade += 1
    if failed_years > 1:
        print(f"{name} has been excluded at {grade + 1} grade")
        break
    if grade == 12:
        print(f"{name} graduated. Average grade: {(total_grade_score / 12):.2f}")
        break