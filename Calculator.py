def add():
    num1= float(input("Enter the value of number 1: "))
    num2= float(input("Enter the value of number 2: "))
    print("Result: ",num1+num2)

def sub():
    num1 = float(input("Enter the value of number 1: "))
    num2 = float(input("Enter the value of number 2: "))
    if num1 < num2:
        temp = num1
        num1 = num2
        num1 = temp
    else:    
        print("Result: ",num1-num2)    

def mul():
    num1= float(input("Enter the value of number 1: "))
    num2= float(input("Enter the value of number 2: "))
    print("Result: ",num1*num2)    

def div():
    num1= float(input("Enter the value of number 1: "))
    num2= float(input("Enter the value of number 2: "))
    print("Result: ",num1/num2)  

def main():
    while True:
        print("""       Welcome to the Simple Calculator!     """)
        print("""            Choose an operation:             """)
        print("""              1. Addition                    """)
        print("""              2. Subtraction                 """)
        print("""              3. Multiplication              """)
        print("""              4. Division                    """)
        print("""              5. Exit                        """)
    
        choice = input("Enter the choice between 1 to 5: ")
        if choice == '5':
            print("Exit")
        elif choice == '1':
            add()
        elif choice == '2':
            sub()        
        elif choice == '3':
            mul()
        elif choice == '4':
            div()   
        else:
            print("Invalid input.Try again: ")      
            choice = input("Enter the choice between 1 to 5: ")
main()            