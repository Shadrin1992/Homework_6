# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

print("Введите номер дня недели: ")
# day_of_week_num = int(input())

# if day_of_week_num == 6 or day_of_week_num == 7:
#     print('Выходной')
# else:
#     print('Не выходной')

day_category = lambda a: print('Выходной') if (a == 6 or a == 7) else print('Не выходной')
print(day_category(int(input())))
