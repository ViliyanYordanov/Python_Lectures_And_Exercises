# first_line = input().split()
# second_line = input().split()
# third_line = input().split()
#
# zero = '0'
# first = '1'
# second = '2'
# first_player_points = 0
# second_player_points = 0
#
# for x in first_line:
#     if x == first:
#         first_player_points += 1
#     elif x == second:
#         second_player_points += 1
#     else:
#         continue
#
# for y in second_line:
#     if y == first:
#         first_player_points += 1
#     elif y == second:
#         second_player_points += 1
#     else:
#         continue
#
# for z in third_line:
#     if z == first:
#         first_player_points += 1
#     elif z == second:
#         second_player_points += 1
#     else:
#         continue
#
# if first_player_points > second_player_points:
#     print("First player won")
# elif first_player_points < second_player_points:
#     print("Second player won")
# else:
#     print("Draw!")


line_1 = input().split()
line_2 = input().split()
line_3 = input().split()

first_player = False
second_player = False

# check rows
for i in range(3):
    if line_1[i] == line_2[i] == line_3[i] == '1':
        first_player = True
    if line_1[i] == line_2[i] == line_3[i] == '2':
        second_player = True

# check columns
for i in range(3):
    if line_1.count('1') == 3 or line_2.count('1') == 3 or line_2.count('1') == 3:
        first_player = True
    if line_1.count('2') == 3 or line_2.count('2') == 3 or line_2.count('2') == 3:
        second_player = True
# check diagonals
if line_1[0] == '1' and line_2[1] == '1' and line_3[2] == '1' or line_1[2] == '1' and line_2[1] == '1' and \
        line_3[0] == '1':
    first_player = True
if line_1[0] == '2' and line_2[1] == '2' and line_3[2] == '2' or line_1[2] == '2' and line_2[1] == '2' and \
        line_3[0] == '2':
    second_player = True

if first_player:
    print('First player won')
elif second_player:
    print('Second player won')
else:
    print('Draw!')