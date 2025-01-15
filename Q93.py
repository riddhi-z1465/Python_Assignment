# Demonstrate encapsulation by creating a class with private attributes and use getter and setter methods to access/modify them.
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    # Getter for balance
    @property
    def balance(self):
        return self.__balance

    # Setter for balance
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = amount

    # Method to deposit money
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount

if __name__ == "__main__":
    account = BankAccount("123456789", 1000)
    print(f"Initial Balance: {account.balance}")

    account.deposit(500)
    print(f"Balance after deposit: {account.balance}")

    try:
        account.balance = -100  # This will raise an error
    except ValueError as e:
        print(e)  # Print the error message