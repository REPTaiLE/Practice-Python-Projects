# Choose Options
def get_option():
    while True:
        try:
            option = int(input(""" 
            Please enter one of the following operations:
            [1] - Check account information
            [2] - Make a deposit
            [3] - Retire money
            [4] - Quit the program
            ------------------------\t

            """))

            if option in range(1, 5):
                print(f"You chose {option}!")
                return option
            else:
                print("Error: You must only choose a number between 1 and 4!")

        except ValueError:
            print("Error: Please, you must enter a valid number!")


class Person:

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


class Client(Person):

    def __init__(self, name, last_name, account_num, balance=0):
        super().__init__(name, last_name)  # Inherit from Person
        self.account_num = account_num
        self.balance = balance

    # Special Methods
    def __str__(self):
        return f"""
            Account Information\n
            Name: {self.name}\n
            Last Name: {self.last_name}\n
            Account Number: {self.account_num}\n
            Balance: {self.balance}\n
        """

    # Deposit and Retirement Methods
    def deposit(self):
        money = float(input("Please, enter the amount of money you want to deposit: "))
        self.balance += money
        print(f"You've successfully deposited {money}. New balance: {self.balance}")

    def retirement(self):
        money = float(input("Please, enter the amount of money you want to withdraw: "))
        if money > self.balance:
            print("Error: You don't have enough funds!")
        else:
            self.balance -= money
            print(f"You've successfully withdrawn {money}. New balance: {self.balance}")


# Execution
def main():
    name = input("Please enter your name: ")
    last_name = input("Please enter your last name: ")
    account_num = int(input("Please enter your account number: "))

    client = Client(name, last_name, account_num, balance=0)

    while True:
        options = get_option()
        if options == 1:
            print(client)
        elif options == 2:
            client.deposit()
        elif options == 3:
            client.retirement()
        elif options == 4:
            print("Exiting the program.")
            break


if __name__ == "__main__":
    main()
