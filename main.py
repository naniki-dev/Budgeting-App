import accounts, transactions, storage
'''
Entry point
- shows menu
- takes user input
- calls other modules
Should not contain any business logic
It is the controller
'''

def main():
    # Check if user has account already
    print("Hello. Do you already have an profile with us?")

    while True:
        choice = int(input("1. Yes. 2. No.\n>> "))

        if choice == 1:
            print("Welcome back.")
            user_id = input("What's your name?\n>> ")
            accounts.get_account(user_id)
            print("What would you like to do?")
            option = int(input("1. Add transaction. 2. View balance. 3. View transactions.\n>> "))
            if option == 1:
                pass
            elif option == 2:
                pass
            elif option == 3:
                pass
            else:
                print("Please enter a valid option.") 

        elif choice == 2:
            print("Welcome, let's create your profile.")
            user_id = input("What's your name?\n>> ")
            # create default parameter for data
            accounts.create_account(user_id)
            print("What would you like to do?")
            option = int(input("1. Add transaction. 2. View balance. 3. View transactions.\n>> "))
            if option == 1:
                pass
            elif option == 2:
                pass
            elif option == 3:
                pass
            else:
                print("Please enter a valid option.") 

        else:
            print("Please enter a valid option.") 

if __name__ == "__main__":
    main()