# define the functions : add, sub, mult, div
# print options to the users
# ask for values
# call the functions
# while loop until the user want to exit

def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "/n")

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer)+ "/n")

def mult(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer)+ "/n")

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer)+ "/n")
while True:
    print("A. Addition")
    print("B. Substraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Que voulez-vous faire ? : ").lower()

    if choice == "a":
        print("Addition")
        a = int(input("premier nombre : "))
        b = int(input("deuxième nombre : "))
        add(a, b)
    elif choice == "b":
        print("Substraction")
        a = int(input("premier nombre : "))
        b = int(input("deuxième nombre : "))
        sub(a, b)
    elif choice == "c":
        print("Multiplication")
        a = int(input("premier nombre : "))
        b = int(input("deuxième nombre : "))
        mult(a, b)
    elif choice == "d":
        print("Division")
        a = int(input("premier nombre : "))
        b = int(input("deuxième nombre : "))
        div(a, b)
    elif choice == "e":
        print("Program ended")
        quit()