print("Program started")
character = str(input("Please enter a standard character"))
if len(character) > 1:
    print("Please enter only one character")
else:
    value = ord(character)
    print(f"The ASCII code for {character} is {value}")
print("Program Ended")

