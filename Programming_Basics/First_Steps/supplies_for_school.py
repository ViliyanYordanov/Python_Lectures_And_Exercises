pen_package = int(input())
marker_package = int(input())
cleaning_agent = int(input())
discount = int(input())

money = ((pen_package * 5.80 + marker_package * 7.20 + cleaning_agent * 1.20) -
         (pen_package * 5.80 + marker_package * 7.20 + cleaning_agent * 1.20) * discount /100)

print(money)
