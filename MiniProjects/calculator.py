num1= float(input("enter first number : "))
num2= float(input("enter first number : "))

def calculator(num1,num2):
    print("press 1 for addition \npress 2 for subtraction \npress 3 for multiplication\npress 4 for divition")
    choice = int(input("enter your choice : "))
    print('num1 :', num1, 'num2 :', num2, 'choice :', choice)
    if choice == 1:
        print(num1 + num2)
    elif choice == 2:
        print(num1 - num2)
    elif choice == 3:
        print(num1 * num2)
    elif choice == 4:
        print(num1 / num2)
    else:
        print("enter number between 1 to 4")
        calculator(num1,num2)
calculator(num1,num2)