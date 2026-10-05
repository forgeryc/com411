adventure = str(input("Enter the type of adventure: "))
if adventure == "short" or "scary":
    print("Entering the dark forest!")
elif adventure == "safe" or "long":
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")

print("What did I hear?")
heard = str(input("> "))
print("What did I see?")
seen = str(input("> "))
if heard == "grrr" and seen == "two red eyes":
    print("There is a scary creature. I should get out of here!")
else:
    print("I am a little scared but I will continue.")