# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# print('Введите координаты первой точки (Х,Y) через запятую: ')
# coord_1 = input().split(',')

# print('Введите координаты второй точки (Х,Y) через запятую: ')
# coord_2 = input().split(',')

# distance = (((int(coord_2[0]) - int(coord_1[0]))**2 + (int(coord_2[1]) - int(coord_1[1]))**2))**0.5

distance = lambda a, b, c, d: (((a-c))**2 + ((b-d)**2))**0.5

print(round(distance(int(input('Введите x1: ')),int(input('Введите y1: ')),int(input('Введите x2: ')),int(input('Введите y2: '))),2))