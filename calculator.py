#taking input number1, while converting to an integer
number1 = int(input("number 1:"))
#taking input number2, while converting to an integer
number2 = int(input("number 2:"))
# taking input op, for operator, and not converting to integer as operator  is not an integer
op = input("operator: ")
#first if statement to check if op is equal to +, remember 2 == sign as 2 = signs  is for comparing and one = sign is for assiging a value
if op == '+':
    #adding the values and printing, while working with variables remeber that you are trying to use the variables for calcultions and not tryingto print the formula itself so no need of quotes
    print(number1 + number2)
#if tthe first if is not correct, it will fall back to the next elif and try to check for the conditions present there, you can add the conditions the same way as if
elif op == '-':
    print(number1 - number2)
# the or operator here checks if either the op == 'x' or the op =='*' condition is true, if either one is then the code in that elif will run
elif op == 'x' or op == '*':
    print(number1 * number2)
#here the and operator checks if all 3 of the conditions given are true, only then will it run the code inside of it
elif op == '/' and number1 != 0 and number2 != 0:
    print(number1 /number2)
#else is your final fall back, if all ifs and elifs are not true, then it executes the code in else
else:
    print('error')
