import json
import os

def main():
    print("Please select an option.")
    choice = int(input("1. Add income. 2. Add expense. 3. View total.\n>> "))
    # choice will call specific function
    if choice == 1:
        amount = get_income()
        add_income(amount)

    elif choice == 2:
        amount = get_expense()
        add_expense(amount)

    elif choice == 3:
        pass

    else:
        print("Enter a valid option.") 

'''
Each function will handle getting user input for amounts & category
'''
def get_income():
    while True:
        try:
            amount = int(input("Enter amount: "))
            if not isinstance(amount, int):
                raise ValueError
            else:
                return amount
        except ValueError:
            print("Only enter numbers.")


def get_expense():
    while True:
        try:
            amount = int(input("Enter amount: "))
            if not isinstance(amount, int):
                raise ValueError
            else:
                return amount
        except ValueError:
            print("Only enter numbers.")



file_path = "data.json"

'''
Each function will handle it's own reading and writing to the file
'''
def add_expense(amount):
    pass


def add_income(amount):
    # print("Which category is this in?")
    # category = input("1. Salary. 2. Allowance. 3. Other.\n>> ")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                data_list = json.load(file)
                if not isinstance(data_list, list):
                    data_list = []  # Make sure it's a list
            except json.JSONDecodeError:
                data_list = []  # File exists but is empty or invalid
    else:
        data_list = []

    # Add new data
    new_data = {"income": amount}
    data_list.append(new_data)

    # Write back to the JSON file
    with open(file_path, "w") as f:
        json.dump(data_list, f, indent=2)
    print("Amount has been added.")


def view_total():
    pass


if __name__ == "__main__":
    main()