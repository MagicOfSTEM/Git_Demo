# Simple Calculator for Git

print('Welcome to this simple calculator')

number1 = float(input("Please enter your 1st number: "))
number2 = float(input("Please enter your 2nd number: "))
operator = input("Please enter the operator/math function: +, -, x, /:  " )

# Simple calculator function
def calc(num1, num2, op):
        if op == '+':
            answer = num1 + num2
        elif op == '-':
            answer = num1 - num2
        elif op == 'x':
            answer = num1 * num2
        elif op == '/':
            answer = num1 / num2
        else:
            print("Inputs not recognised, please try again")
        return print(answer)
    
calc(number1, number2, operator)