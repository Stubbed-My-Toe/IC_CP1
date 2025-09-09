#IC 1st period Calculator

print("What is your first number?")
number1 = int(input())

print("What is your second number?")
number2 = int(input())

multiplication = int(number1 * number2)
division = int(number1 / number2)
addition = int(number1 + number2)
subtraction = int(number1 - number2)
int_division = int(number1 // number2)
modulo = int(number1 % number2)
exponents = int(number1 ** number2)

round(multiplication, 2)
round(division, 2)
round(addition, 2)
round(subtraction, 2)
round(int_division, 2)
round(modulo, 2)
round(exponents, 2)

print(f"{number1} * {number2} = ,{multiplication}")
print(f"{number1} / {number2} = {division}")
print(f"{number1} + {number2} = {addition}")
print(f"{number1} - {number2} = {subtraction}")
print(f"{number1} + {number2} = {int_division}")