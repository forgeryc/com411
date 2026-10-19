from collections.abc import Iterable


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


def display_ladder(steps):
    for i in range(steps):
        print("""
        | |
        ***
        """
        )


def create_ladder():
    num = int(input("Enter the number of steps: "))
    return num


def sum_weights(c_weight, i_weight):
    return c_weight + i_weight


def calc_weight(c_weight, i_weight):
    avg = c_weight + i_weight / 2
    return avg


def run():
    c_weight = int(input("What is the weight of the person? \n "))
    i_weight = int(input("What is the weight of their inventory? \n "))
    option = str(input("What would you like to calculate (sum or average)? \n "))
    if option.lower() == "sum":
            sum = sum_weights(c_weight, i_weight)
            print(f"The sum is: {sum}")
    elif option.lower() == "average":
        avg = calc_weight(c_weight, i_weight)
        print(f"The average is: {avg}")
    else:
        print("No valid option entered")

def boxIt():
    pr

def word_manipulation():
    word = str(input("Enter a word: "))
    print("""
    What would you like to do:
    1) Display in a Box – display the word in an ASCII art box
    2) Display Lower-case – display the word in lower-case e.g. hello
    3) Display Upper-case – display the word in upper-case e.g. HELLO
    4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH
    5) Repeat – ask the user how many times to display the word and then display the
    word that many times alternating between upper-case and lower-case.
    """)

