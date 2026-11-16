"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""
def sanitise(input):
    # .lower() converts the inputs to lowercase for Sanitisation
    # .strip() removes whitespace for sanitisation
    input.lower()
    input.strip()

def title_screen(title):
    dashes = ""
    for _ in range(len(title.strip())):
        dashes += "-"
    show_title = f"""{dashes}
{title}
{dashes}
    """
    title.strip()
    print(show_title)


def menu(choice1, choice2):

    show_menu = str(input(f"""
    Please enter the letter which corresponds with your desired menu choice:
    [A] {choice1}
    [B] {choice2}
    [X] Exit
    """))
    sanitise(show_menu)
    if confirm_response(show_menu) == True:
        if show_menu == "x":
            return None
        elif show_menu == "a":
            print(f"You have chosen option A - {choice1}")
            return "a"
        elif show_menu == "b":
            print(f"You have chosen option B - {choice2}")
            return "b"
        else:
            print("Invalid option - please enter a valid input")
            menu(choice1, choice2)
    else:
        menu(choice1, choice2)

def confirm_response(option):
    print(f"You have chosen option {option}")
    confirm = str(input(f"Are you sure you want to proceed with option {option}? (y/n) "))
    confirm.lower()
    if confirm == "y":
        return True
    elif confirm == "n":
        return False
    else:
        print("Invalid option - please enter a valid input (y/n")
        confirm_response(option)
        return None


def view_data():
    show_menu = str(input("""Please enter one of the following options:
        [A] View Reviews by Park
        [B] Number of Reviews by Park and Reviewer Location
        [C] Average Score per year by Park
        [D] Average Score per Park by Reviewer Location
        [X] Exit
        """))
    sanitise(show_menu)
    if confirm_response(show_menu) == True:
        if show_menu == "x":
            return None
        elif show_menu == "a":
            reviews_by_park("disney")

def visualise_data():
    show_menu = str(input(f"""
        Please enter the letter which corresponds with your desired menu choice:
        [A] Most Reviewed Parks
        [B] Park Ranking by Nationality
        [C] Most Popular Month by Park
        [X] Exit
        """))

def reviews_by_park(park1):
    which = str(input(f"""Which park would you like to see reviews for?
    [A] $(park1)
    [X] Exit
     """))
    sanitise(which)
    if which == "x"
        return 0
    elif which == "a":
        # put here printing the entire file.
    else:
        print("Invalid option - please enter a valid input (A/X")
        reviews_by_park(park1)

def number_of_reviews(park, reviewer):
