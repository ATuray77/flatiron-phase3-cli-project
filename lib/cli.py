from simple_term_menu import TerminalMenu
from prettycli import red, yellow, green, blue
from models import Owner, Car
from prompt_toolkit import prompt
#import prompt
#import ipdb; ipdb.set_trace()

class Cli():

    class Prompt():
        def ask(self, question):
            value = input(question)
            return value
        # Addition
        def yes_or_no(self, question):
            value = input(question + "y/n")
            return value == "y"
        # get_car
        def ask(self, question):
            value = input(question)
            return value
            
    
    def __init__(self):
        current_owner = None
        

    def start(self):
        self.clear_screen(20)
    
        logged_in = False
        
        

        print(yellow("WELCOME TO TURAY'S PARKING GARAGE!\n"))
        print(blue("Please make a selection:"))
        options = ["Login", "Car Owner", "New Customer", "Add a car", "Exit!"]
        if logged_in:
            options.append("Login")

        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        #print("The index of the option we chose was:", menu_entry_index)
        print(green(f"You have selected {options[menu_entry_index]}!"))

        self.get_first_name()
        self.get_car()

    def clear_screen(self, lines):
        print("\n" * lines)

    
    
    def get_first_name(self):
        name = prompt("What is your first name? ")
        yes_no = prompt(f"You entered {name}, is that correct y/n: ")
        print(f"WELCOME, {name}")

        # if yes_no:
        #     print("Collect last_name")
        # else:
        #     self.get_first_name()
    
    def get_car(self):
        mycar = prompt("What's the name of your car? ")
        print(f"Yes, we have your {mycar}")


        

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