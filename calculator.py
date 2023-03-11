import argparse

parser = argparse.ArgumentParser(description = "Available operations are: +, -, /, *, mod, pow, div")
args = parser.parse_args() 

while True:
    try:
        n1 = float(input('Enter your first value: '))
        operation = input('Enter operation: ')
        n2 = float(input('Enter your second value: '))
        break
    except ValueError:
        print("Only digits allowed as a value!")
        continue

if operation in ['/', 'mod', 'div'] and n2 == 0:
    print('Division by zero!')
elif operation == '+':  print(n1 + n2)
elif operation == '-':  print(n1 - n2)
elif operation == '/':  print(n1 / n2)
elif operation == '*':  print(n1 * n2)
elif operation == 'mod':    print(n1 % n2)
elif operation == 'pow':    print(n1 ** n2)
elif operation == 'div':    print(n1 // n2)

   