# Simple Calculator for Git

print('Welcome to this simple calculator')
print('Type \"Q\" to quit calculator')

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
        return print(f'{num1} {op} {num2} = {answer:.4f}') # Rounded result to 2dp

# Added continuous run with exit option
re_run = " "
while re_run != "q":
    try: # Add error handling (Issue1)
        number1 = float(input("Please enter your 1st number: "))
        number2 = float(input("Please enter your 2nd number: "))
        operator = " "
        while operator not in ("+", "-", "x", "/"):
            operator = input("Please enter the operator/math function: +, -, x, /:  " )
        calc(number1, number2, operator)

    except:
        print("Possible typo, please re-enter the options")
    
    re_run = input("Press any key to continue, or \'Q\' to exit: ").lower()