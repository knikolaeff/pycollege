print('Enter your shape: a triangle, a rectangle or a circle')
shape = input('Shape: \n')
shape = shape.lower()
if shape == 'triangle':
    print('Enter sides of the triangle')
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
elif shape == 'rectangle':
    print('Enter sides of the rectangle')
    a = int(input())
    b = int(input())
    S = a * b 
elif shape == 'circle':
    print('Enter radius of the circle')
    r = int(input())
    S = 3.14 * r ** 2 
print(S)
