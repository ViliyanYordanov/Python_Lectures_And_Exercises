movie = input()
total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while movie != 'Finish':
    capacity = int(input())
    ticket_counter = 0
    ticket_type = input()
    while ticket_type != 'End':
        if ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'kid':
            kid_tickets += 1

        ticket_counter += 1
        total_tickets += 1
        if ticket_counter == capacity:
            break
        ticket_type = input()
    volume_capacity = ticket_counter / capacity * 100
    print(f"{movie} - {volume_capacity:.2f}% full.")

    movie = input()

students = student_tickets / total_tickets * 100
standards = standard_tickets / total_tickets * 100
kids = kid_tickets / total_tickets * 100
print(f"Total tickets: {total_tickets}")
print(f"{students:.2f}% student tickets.")
print(f"{standards:.2f}% standard tickets.")
print(f"{kids:.2f}% kids tickets.")