max_failed_problems = int(input())
failed_problems = 0
last_problem = ''
score = 0
number_of_problems = 0

while True:
    current_problem = input()
    if current_problem == 'Enough':
        average_score = score / number_of_problems
        print(f"Average score: {average_score:.2f}")
        print(f"Number of problems: {number_of_problems}")
        print(f"Last problem: {last_problem}")
        break
    current_grade = int(input())
    score += current_grade
    number_of_problems += 1
    last_problem = current_problem

    if current_grade <= 4:
        failed_problems += 1
        if failed_problems == max_failed_problems:
            print(f"You need a break, {failed_problems} poor grades.")
            break