# Calculator

a = float(input("Enter 1st number: "))

op = input("Enter operator (+, -, *, /, %, **): ")

b = float(input("Enter 2nd number: "))

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
elif op == '%':
    print(a % b)
elif op == '**':
    print(a ** b)
else:
    print("invalid operator")