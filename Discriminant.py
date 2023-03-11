import math

def Discriminant(a, b, c):
    D = b ** 2 - 4 * a * c
    print(f"Discriminant equals to: {str(D)}")
    if D < 0:
        return ("No roots!")
    if D == 0:
        return(-b / (2 * a))
    return (-b + math.sqrt(D)) / (a * 2), ((-b - math.sqrt(D)) / (a * 2))

while True: 
    a = float(input("Enter your 'a' value: "))
    b = float(input("Enter your 'b' value: "))
    c = float(input("Enter your 'c' value: "))
    print(Discriminant(a, b, c))
    answer = input("Solve one more equation? (y/n): ")
    continue

