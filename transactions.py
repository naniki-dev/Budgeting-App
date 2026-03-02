'''
Manage transactions
Responsible for:
- add transaction
- calculate totals
- filter transactions
'''


file_path = "data.json"

def add_transaction(account_id, type, amount, category):
    # It will call the file functions inside
    pass 

def calculate_balance(account_id):
    pass

def get_transactions(account_id):
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
    new_data = {}
    # Check if ID is in list, if not then add new ID else update current one
    for account in data_list:
        # If ID is in there then update 
        pass
        # create new one
  
    new_data = {"income": amount}
    data_list.append(new_data)

    # Write back to the JSON file
    with open(file_path, "w") as f:
        json.dump(data_list, f, indent=2)
    print("Amount has been added.")


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
