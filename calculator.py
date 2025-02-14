def calculator():
    num1=int(input("input num1 >"))
    operand=input('+,-,*,/,')
    num2=int(input("input num2 >"))
    if operand == '+':
        print(num1+num2)
    elif operand == '-':
        print(num1+num2)
    elif operand == '*':
        print(num1*num2)
    else:
        print(num1/num2)
   
calculator()