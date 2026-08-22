class BankAccount:
    bank_name = "TBC Bank"
    __total_accounts = 0

    def __init__(self, owner, balance=0):
        self._owner = owner
        self.__balance = balance if self.validate_amount(balance) else 0
        BankAccount.__total_accounts += 1
        self.__account_number = f"AN{BankAccount.__total_accounts:04d}"

    def deposit(self, amount):
        if self.validate_amount(amount):
            self.__balance += amount
            return self.__balance
        print("თანხა უნდა იყოს დადებითი!")

    def withdraw(self, amount):
        if self.validate_amount(amount):
            if self.__balance >= amount:
                self.__balance -= amount
                return self.__balance
            print("არასაკმარისი ბალანსი!")
        else:
            print("თანხა უნდა იყოს დადებითი!")

    def check_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def change_owner(self, new_owner):
        self._owner = new_owner

    @classmethod
    def get_total_accounts(cls):
        return cls.__total_accounts

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    def __str__(self):
        return f"Account: {self.__account_number} | Owner: {self._owner}"


# დემონსტრაცია
if __name__ == "__main__":
    acc1 = BankAccount("Zviangi Shavkverashvili", 500)
    acc2 = BankAccount("Giorgi Kabanashvili", 1200)
    
    print(acc1)
    print(acc2)

    acc1.deposit(200)
    print(f"acc1 ბალანსი შევსების შემდეგ: {acc1.check_balance()}")

    acc1.withdraw(100)
    print(f"acc1 ბალანსი გამოტანის შემდეგ: {acc1.check_balance()}")

    acc1.change_owner("Zviangi Shavkverashvili")
    print(f"განახლებული acc1: {acc1}")

    print(f"სულ ანგარიშები: {BankAccount.get_total_accounts()}")
