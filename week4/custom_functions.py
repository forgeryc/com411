def listen():
    sound = str(input("Enter a sound: "))
    print(f"That was a loud {sound}!")


def identify():
    vision = str(input("What do you see: "))
    if vision.lower() == " a large boulder":
        print("It's time to run!")
    else:
        print("We will be fine")


def escape_by(plan):
    if plan.lower() == "jumping over"):
        print("We can't escape that way!")
    elif plan.lower() == "running around":
        print("We cannot escape that way!, the boulder is moving too fast!")
    elif plan.lower() == "cross bridge ahead":
        print("That might just work! Let's go!")
    else:
        print("We cannot escape that way!, the boulder is in the way!")


escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")