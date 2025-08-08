def addition(x,y): 
    return x + y

def substraction(x,y):
    return x - y

def multiplication(x,y):
    return x*y

def division(x,y):
    if y != 0:
        return x/y
    else:
        print('You cannot divide by 0! ')
    
def main():
    print('Choose the operation: (1/2/3/4)') 
    print('1 Addition ')
    print('2 Substraction ')
    print('3 Multiplication ')
    print('4 Division ')
    option = input()

    num1 = float(input('Introduce your first number: '))
    num2 = float(input('Introduce your second number: '))

    if option == '1':
        print('The result is: ' ,addition(num1,num2))
    elif option == '2':
        print('The result is: ' ,substraction(num1,num2))
    elif option == '3':
        print('The result is: ' ,multiplication(num1,num2))
    elif option =='4':
        print('The result is: ' ,division(num1,num2))
    else:
        print('Invalide operation')

if __name__ == '__main__':
    main()