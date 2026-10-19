def listen():
    sound = str(input("Enter a sound: "))
    print(f"That was a loud {sound}!")


def identify():
    vision = str(input("What do you see: "))
    if vision.lower() == " a large boulder":
        print("It's time to run!")
    else:
        print("We will be fine")
identify()