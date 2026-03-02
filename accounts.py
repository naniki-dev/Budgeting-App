'''
Only manage account logic
Do not calculate totals
Responsible for:
- find account by ID
- create new account
- return account object
'''
file_path = "data.json"

def get_account(account_id, data = file_path):
    for account in data:
        if account["ID"] == account_id:
            return account

def create_account(account_id, data = file_path):
    account = {"ID": account_id }
    # return account or call storage function
    return account

