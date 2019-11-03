expression = input("Enter an expression: ").split(" ")
operator = expression[1]
arg0 = expression[0]
arg1 = expression[2]


def add(num1, num2):
    return int(num1) + int(num2)


def subtract(num1, num2):
    return int(num1) - int(num2)


def mult(num1, num2):
    return int(num1) * int(num2)


def div(num1, num2):
    return int(num1) / int(num2)


def power(num1, num2):
    return pow(int(num1), int(num2))


if operator == '+':
    print(add(arg0, arg1))
elif operator == '-':
    print(subtract(arg0, arg1))
elif operator == '*':
    print(mult(arg0, arg1))
elif operator == '/':
    print(div(arg0, arg1))
else:
    print(power(arg0, arg1))
