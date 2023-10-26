number_of_student = int(input())
students_with_2 = 0
students_with_3 = 0
students_with_4 = 0
students_with_5 = 0
all_students = 0
total_grade = 0


for _ in range(number_of_student):
    student_grade = float(input())

    if 2.00 <= student_grade < 3.00:
        students_with_2 += 1
        total_grade += student_grade
    elif 3.00 <= student_grade < 4.00:
        students_with_3 += 1
        total_grade += student_grade
    elif 4.00 <= student_grade < 5.00:
        students_with_4 += 1
        total_grade += student_grade
    elif student_grade >= 5.00:
        students_with_5 += 1
        total_grade += student_grade

all_students = students_with_5 + students_with_4 + students_with_3 + students_with_2

print(f"Top students: {students_with_5 / all_students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {students_with_4 / all_students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {students_with_3 / all_students * 100:.2f}%")
print(f"Fail: {students_with_2 / all_students * 100:.2f}%")
print(f"Average: {total_grade / all_students:.2f}")
