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
    if plan.lower() == "jumping over":
        print("We can't escape that way!")
    elif plan.lower() == "running around":
        print("We cannot escape that way!, the boulder is moving too fast!")
    elif plan.lower() == "cross bridge ahead":
        print("That might just work! Let's go!")
    else:
        print("We cannot escape that way!, the boulder is in the way!")


def cross_bridge(distance):
    for i in range(distance):
        if i <= 5:
            print("Crossed step")
        else:
            print("The bridge is collapsing!")
            return 0
    print("We must keep going")
    return 1


def climb_ladder(steps_remain, steps_crossed):
    if steps_remain > steps_crossed:
        print("Still some way to go!")
    else:
        print("We are almost there")


climb_ladder(5, 2)
climb_ladder(2, 5)
