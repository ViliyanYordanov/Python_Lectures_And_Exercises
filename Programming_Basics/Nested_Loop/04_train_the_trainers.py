number_of_judges = int(input())
presentation_counter = 0
total_score = 0
presentation = input()

while presentation != 'Finish':
    presentation_counter += 1
    current_presentation_score = 0
    for _ in range(1, number_of_judges + 1):
        score = float(input())
        current_presentation_score += score

    average = current_presentation_score / number_of_judges
    total_score += average
    print(f"{presentation} - {average:.2f}.")
    presentation = input()

print(f"Student's final assessment is {(total_score / presentation_counter):.2f}.")