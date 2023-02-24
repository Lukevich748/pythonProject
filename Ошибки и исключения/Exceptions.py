import math

#Кастомный тип исключения
class InvalidTriangleError(Exception):
    """Raised when a triangle has invalid sides"""

#Функция вычисления площади треугольника
def calc_square(ab, ac, bc):
    if ab <= 0 or ac <= 0 or bc <= 0:
        raise InvalidTriangleError('Число должно быть больше 0')

    p = (ab + ac + bc) / 2
    s = math.sqrt(p * (p - ab) * (p - ac) * (p - bc))
    return s

square = calc_square(-2, 8, 8)
print(square)