from simple_term_menu import TerminalMenu
from ipdb import ipdb; ipdb.set_trace()

def main():
    print("WELCOME TO TURAY'S PARKING GARAGE!\n")
    options = ["Car Owner", "New Customer", "Add a car", "Exit!"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    user_input = input("Please make a selection")
    print(f"You have selected {options[menu_entry_index]}!")

    handle_user_input(user_input)

    def handle_user_input(input):
        import ipdb; ipdb.set_trace()


if __name__ == "__main__":
    main()


# def start():
#     print("WELCOME TO TURAY'S PARKING GARAGE!\n")
#     print("1. My Toys")
#     print("2. Add Toy")
#     print("3. Exit")
#     user_input = input("Please make a selection (1-3)")


    
# start()