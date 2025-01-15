# Create a class with a private attribute _balance and provide get_balance() and set_balance() methods.
class Account:
    def __init__(self, initial_balance=0):
        """Initialize the account with a given balance."""
        self._balance = initial_balance  # Private attribute

    def get_balance(self):
        """Return the current balance."""
        return self._balance

    def set_balance(self, amount):
        """Set the balance to a new value."""
        if amount < 0:
            print("Balance cannot be negative.")
        else:
            self._balance = amount

account = Account(100)  # Create an account with an initial balance of 100

# Get the current balance
print("Current Balance:", account.get_balance())  # Output: Current Balance: 100

# Set a new balance
account.set_balance(200)
print("Updated Balance:", account.get_balance())  # Output: Updated Balance: 200

# Attempt to set a negative balance
account.set_balance(-50)  # Output: Balance cannot be negative.
print("Balance after attempting to set negative:", account.get_balance())  # Output: Updated Balance: 200