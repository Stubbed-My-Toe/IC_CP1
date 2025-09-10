#IC 1st period Calculator

print("What is your first number?")
number1 = float(input())

print("What is your second number?")
number2 = float(input())

raw_multiplication = float(number1 * number2)
raw_division = float(number1 / number2)
raw_addition = float(number1 + number2)
raw_subtraction = float(number1 - number2)
raw_int_division = float(number1 // number2)
raw_modulo = float(number1 % number2)
raw_exponents = float(number1 ** number2)

multiplication = round(raw_multiplication, 2)
division = round(raw_division, 2)
addition = round(raw_addition, 2)
subtraction = round(raw_subtraction, 2)
int_division = round(raw_int_division, 2)
modulo = round(raw_modulo, 2)
exponents = round(raw_exponents, 2)

print(f"{number1} * {number2} = {multiplication}")
print(f"{number1} / {number2} = {division}")
print(f"{number1} + {number2} = {addition}")
print(f"{number1} - {number2} = {subtraction}")
print(f"{number1} // {number2} = {int_division}")
print(f"{number1} % {number2} = {modulo}")
print(f"{number1} ** {number2} = {exponents}")