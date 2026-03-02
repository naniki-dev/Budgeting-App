import json
import os

'''
Responsible for:
- open file
- load data
- save data
- handle empty/missing file
These functions only deal with JSON file
Only job is to read and write data
Nothing about income or expenses
'''

file_path = "data.json"

def load_data(data = file_path):
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
    
    return data_list

data_list = load_data()

def save_data(data = file_path):
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

