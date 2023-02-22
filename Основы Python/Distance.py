import math

print('Введите координаты первой точки:')

print('Введите х1:')
x1 = float(input())

print('Введите y1:')
y1 = float(input())

point_1 = [x1, y1]

print('Введите координаты второй точки:')
print('Введите х2:')
x2 = float(input())

print('Введите y2:')
y2 = float(input())

point_2 = [x2, y2]

print('Расстояние между точками:')
dist = (math.dist(point_1, point_2))
dist = round(dist, 3)
print (dist)