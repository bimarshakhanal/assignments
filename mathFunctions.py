def addition(a,b):
    '''Function to find sum of numbers.'''
    return a+b

def subtraction(a,b):
    '''Function to find difference between two numbers.'''
    return a-b

def multiplication(a,b):
    '''Function to find product of two numbers'''
    return a*b

if __name__=="__main__":
    print("*"*5,"Math Operation","*"*5)
    print("1. Addition\n2. Subtraction\n3. Mulitplication\n4. Exit")
    ch = input("Enter your choice: ")
    if ch=='4':
        quit()
        
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if ch=='1':
        result = addition(a,b)
        print("Sum is ",result)
    elif ch=='2':
        result = subtraction(a,b)
        print("Difference is ",result)
    elif ch=='3':
        result = multiplication(a,b)
        print("Product is ",result)
    else:
        print("Invalid Input")
