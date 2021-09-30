print('Введите фигуру: треугольник, прямоугольник или круг')
shape = input('Фигура: \n')
shape = shape.lower()
if shape == 'треугольник':
    print('Введите стороны треугольника')
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
elif shape == 'прямоугольник':
    print('Введите стороны прямоугольника')
    a = int(input())
    b = int(input())
    S = a * b 
elif shape == 'круг':
    print('Введите радиус круга')
    r = int(input())
    S = 3.14 * r ** 2 
print(S)