def books():
    type = str(input("What type of book is this? \n"))
    if type == "adventure":
        print("I like adventure books!")
        print("Finished reading book.")

activity = str(input("Please enter the activity to be performed.\n"))
if activity == "calculate":
    print("Performing calculations...")
else:
    print("Performing Activity...")

print("Activity Completed!")
