# Create a bank account class and apply the following methods as required
# Deposit/Withdraw
# View Account Details: Method to display the account owner's details and current balance.
# Change Account Owner: Method to update the account owner's information.
# Account Statement: Method to generate a statement of recent transactions.
# Set Overdraft Limit: Method to set an overdraft limit for the account.
# Interest Calculation: Method to calculate and apply interest to the balance.
# Freeze/Unfreeze Account: Methods to freeze and unfreeze the account for security reasons.
# Transaction History: Method to retrieve the history of all transactions made on the account.
# Set Minimum Balance: Method to enforce a minimum balance requirement.
# Transfer Funds: Method to transfer funds from one account to another.
# Close Account: Method to close the account and perform necessary cleanup. 


class Bank_Account:
    def __init__(self, account_number, account_balance, account_holder, other_account_number):
        self.account_number = account_number
        self.other_account_number = other_account_number
        self.account_balance = account_balance
        self.account_holder = account_holder
        self.overdraft_limit = 0
        self.is_frozen = False
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            self.transaction_history.append(f"Deposit of {amount} is successful.")
            return f"Deposit of {amount} is successful."
        else:
            return f"{amount} is invalid."

    def withdraw(self, amount):
        if self.account_balance + self.overdraft_limit >= amount:
            self.account_balance -= amount
            self.transaction_history.append(f"{self.account_holder} withdrew {amount}.")
            return f"Withdrawal of {amount} is successful."
        else:
            return f"Insufficient funds. Please top up."

    def check_balance(self):
        return f"Current balance for account {self.account_number} is {self.account_balance}."

    def generate_account_statement(self):
        account_statement = f"The account number is {self.account_number}\n"
        account_statement += f"The account balance is {self.account_balance}\n"
        account_statement += f"The account transactional history is:\n{self.transaction_history}\n"
        return account_statement

    def set_overdraft_limit(self, overdraft_limit):
        self.overdraft_limit = overdraft_limit
        return f"Overdraft limit set to {overdraft_limit}."

    def apply_interest(self, interest_rate):
        self.account_balance += self.account_balance * interest_rate
        return f"Interest applied successfully."

    def freeze_account(self):
        self.is_frozen = True
        return "Account has been frozen."

    def unfreeze_account(self):
        self.is_frozen = False
        return "Account has been unfrozen."

    def retrieve_transaction_history(self):
        return self.transaction_history

    def set_minimum_balance(self, minimum_balance):
        self.minimum_balance = minimum_balance
        return f"Minimum balance set to {minimum_balance}."

    def transfer_balance(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            self.transaction_history.append(f"Transferred {amount} to account {self.other_account_number}")
            return f"Transfer of {amount} to account {self.other_account_number} is successful."
        else:
            return "Insufficient balance for transfer."

    def close_account(self):
        self.account_balance = 0
        self.is_frozen = True
        self.transaction_history = []
        return "Account is closed."

# Creating bank accounts
account1 = Bank_Account("123321123321", 2000, "Gloria Nyaga", "112233445566")
account2 = Bank_Account("112233445566", 0, "Oyanga Kinoti", "123321123321")

# Operations
operations = [
    {"method": "deposit", "args": (1000,), "expected_output": "Deposit of 1000 is successful."},
    {"method": "apply_interest", "args": (0.15,), "expected_output": "Interest applied successfully."},
    {"method": "freeze_account", "args": (), "expected_output": "Account has been frozen."},
    {"method": "retrieve_transaction_history", "args": (), "expected_output": []},
    {"method": "set_minimum_balance", "args": (200,), "expected_output": "Minimum balance set to 200."},
    {"method": "close_account", "args": (), "expected_output": "Account is closed."},
]

for op in operations:
    result = getattr(account1, op["method"])(*op["args"])
    print(result)
    if isinstance(op["expected_output"], str):
        assert result == op["expected_output"], f"Expected '{op['expected_output']}' but got '{result}'"

# Displaying the final account statement
print(account1.generate_account_statement())
