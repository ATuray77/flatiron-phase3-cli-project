from simple_term_menu import TerminalMenu
from prettycli import  red, yellow, green, blue, white, cyan, magenta
from prettycli.colorizer import bright_yellow
from models import Owner, Car
from prompt_toolkit import prompt
from banner import Banner
import re
import time
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

        # def handle_login(self, Login):   #Testing
        #     print("Loggin in")

    
    def __init__(self):
        current_owner = None
        

    def start(self):
        self.clear_screen(20)
        banner = Banner()
        banner.welcome()
    
        logged_in = False
        
        

        print(bright_yellow("WELCOME TO TURAY'S PARKING GARAGE!\n").bold())
        print(blue("Please make a selection:"))
        options = ["Login", "Exit!"]
        for menu_entry_index in range(len(options)):  #testing
            if logged_in:
                options.append("Login")

        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        #print("The index of the option we chose was:", menu_entry_index)
        print(green(f"You have selected {options[menu_entry_index]}!"))
        if options[menu_entry_index] == "Login":
            self.handle_login()
            #get an email
            #find owner by email

        elif options[menu_entry_index] == "Car Owner":
            self.get_first_name()
            self.get_car()
        elif options[menu_entry_index] == "New Customer": # testing new addition new failure
            self.add_a_car()
        else:
            self.exit()
            
            
        


        #import ipdb; ipdb.set_trace()

    def handle_login(self):    #testing
        email = prompt("Please enter your email:\n")
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, email):
            print("Find a user by email")
       
            owner = Owner.find_or_create_by(email) #find owner by email
            #print(f"Hello,{owner.email}")

            self.current_owner = owner
            
            print(cyan(f"Hello, {owner.first_name}! {owner.email} 👋"))
            
            self.show_owner_options()
            
        else:
            print(red("Invalid email. Please try again!")) 
            time.sleep(2)
            self.start()

    #creating get_owner_cars - WORK-IN-PROGRESS
    def get_owner_cars(self):
        email = prompt("Please enter your email so you can see all your cars:\n")
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, email):
            owner = Owner.find_my_cars(email)
            
            self.current_owner = owner
            print(f"Cars owned by {owner.first_name} {owner.last_name}:")
        for car in owner.cars:
            print(f"{car.make_model}, {car.color}, {car.license_plate}")
     
    #creating get_owner_cars - WORK-IN-PROGRESS



    #under construction
    def show_owner_options(self):
        options = ["Car Owner", "New Customer","Exit!"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show() 
        
        print(options[menu_entry_index])
        #print("The index of the option we chose was:", menu_entry_index)
        print(green(f"You have selected {options[menu_entry_index]}!"))
        if options[menu_entry_index] == "Login":
            self.handle_login()
            #get an email
            #find owner by email

        elif options[menu_entry_index] == "Car Owner":
            self.get_owner_cars()
            # self.get_first_name()
            # self.get_car()
        elif options[menu_entry_index] == "New Customer": # testing new addition new failure
            self.add_a_car()
        else:
            self.exit()
    # top is under construction   
    
    def add_a_car(self): # testing new failure
        newcus = prompt("Enter your first_name last_name username phone email: ")
        newcar = prompt("Enter car make_model " "color " "license_plate: ")
        print(f"Adding your profile: {newcus}") 
        print(f"Adding your car to our parking garage: {newcar}")
        self.start()

    def exit(self):
        print(magenta("Bye!"))
    
        

        # self.get_first_name()
        # self.get_car()


    def clear_screen(self, lines):
        print("\n" * lines)

    
    
    def get_first_name(self):
        name = prompt("What is your first name? ")
        #yes_no = prompt(f"You entered {name}, is that correct y/n: ")
        print(f"WELCOME, {name}")
        #self.start()

      
    
    def get_car(self):
        mycar = prompt("What's the name of your car? ")
        print(f"Yes, we have your {mycar}")
        self.start()
   


        

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