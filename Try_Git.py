# Simple Calculator for Git

print('Welcome to this simple calculator')


number1 = input("Please enter your 1st number: ")
number2 = input("Please enter your 2nd number: ")
operator = input("Please enter the operator/math function: +, -, x, /:  " )

# Add error handling (Issue1)
try:
    f_number1 = float(number1)
except:
    print("Input type error! Please enter numbers only")
    number1 = input("Please enter your 1st number: ")
    
try:
    f_number2 = float(number2)
except:
    print("Input type error! Please enter numbers only")
    number2 = input("Please enter your 2nd number: ") 

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

calc(f_number1, f_number2, operator)