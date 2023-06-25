import math
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
** for power
% for modulo
sin for sine
cos for cosine
tan for tangent
sqrt for square root
log for logarithm
''')

    if operation == 'sin' or operation == 'cos' or operation == 'tan' or operation == 'sqrt' or operation == 'log':
        num = float(input('Enter the number: '))
        if operation == 'sin':
            print(math.sin(num))
        elif operation == 'cos':
            print(math.cos(num))
        elif operation == 'tan':
            print(math.tan(num))
        elif operation == 'sqrt':
            print(math.sqrt(num))
        elif operation == 'log':
            print(math.log(num))

    else:
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))

        if operation == '+':
            print(num1 + num2)

        elif operation == '-':
            print(num1 - num2)

        elif operation == '*':
            print(num1 * num2)

        elif operation == '/':
            print(num1 / num2)

        elif operation == '**':
            print(num1 ** num2)

        elif operation == '%':
            print(num1 % num2)

        else:
            print('You have not typed a valid operator, please run the program again.')
    
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()

    elif calc_again.upper() == 'N':
        print('See you later.')

    else:
        again()

calculate()
