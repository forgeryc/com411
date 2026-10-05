def books():
    type = str(input("What type of book is this? \n"))
    if type == "adventure":
        print("I like adventure books!")
        print("Finished reading book.")


def calculate():
    activity = str(input("Please enter the activity to be performed.\n"))
    if activity == "calculate":
        print("Performing calculations...")
    else:
        print("Performing Activity...")
    print("Activity Completed!")


def isEven():
    num = int(input("Please enter a whole number.\n"))
    iseven = True if num % 2 == 0 else False
    if iseven == True:
        print(f"The number {num} is even.")
    else:
        print(f"The number {num} is odd.")


num1 = int(input("Please enter the first number.\n"))
num2 = int(input("Please enter the second number.\n"))
if num1 == num2:
    print("Both are equal!")
elif num1 > num2:
    print("The second number is smallest")
else:
    print("The first number is the smallest")
