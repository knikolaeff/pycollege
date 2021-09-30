import argparse
if (operation == '/' or operation == 'mod' or operation == 'div') and n2 == 0:
    print('Деление на 0!')
elif operation == '+':  print(n1 + n2) 
elif operation == '-':  print(n1 - n2)
elif operation == '/':  print(n1 / n2)
elif operation == '*':  print(n1 * n2)
elif operation == 'mod':    print(n1 % n2)
elif operation == 'pow':    print(n1 ** n2)
elif operation == 'div':    print(n1 // n2)