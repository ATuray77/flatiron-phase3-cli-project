from simple_term_menu import TerminalMenu
from prettycli import red, yellow, green
from models import Owner, Car
#import ipdb; ipdb.set_trace()

class Cli():

    

    def start(self):
        logged_in = True

        print(yellow("WELCOME TO TURAY'S PARKING GARAGE!\n"))
        options = ["Sign Up", "Car Owner", "New Customer", "Add a car", "Exit!"]
        if logged_in:
            options.append("Login")

        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print("The index of the option we chose was:", menu_entry_index)
        print(green(f"You have selected {options[menu_entry_index]}!"))

    


if __name__ == "__main__":
    
    app = Cli()
    app.start()


# def start():
#     print("WELCOME TO TURAY'S PARKING GARAGE!\n")
#     print("1. My Toys")
#     print("2. Add Toy")
#     print("3. Exit")
#     user_input = input("Please make a selection (1-3)")

    # handle_user_input(user_input)

    # def handle_user_input(input):
    #    is_number = input.isdigit()
    #    if is_number:
    #        selection = int(input)
    #        import ipdb; ipdb.set_trace()


# start()