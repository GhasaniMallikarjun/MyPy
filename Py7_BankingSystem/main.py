import random
import os

class Bank:
    def __init__(self):
        self.user_accounts={}
        self.transaction_history={}

    def create_account(self,name, initial_deposit):
        account_id=self._generate_account_number()
        new_account=BankAccount(account_id, name, initial_deposit)
        self.user_accounts[account_id]=new_account
        self.transaction_history[account_id]=[]
        return new_account


    def _generate_account_number(self):
        return "".join(random.choice("0123456789") for _ in range(8))

    def get_account(self, account_id):
        return self.user_accounts.get(account_id)

    def perform_transaction(self, account_id,transaction_type, amount):
        account=self.get_account(account_id)

        if not account:
            return "Account Not Found"


        if transaction_type=="deposite":
             account.deposit(amount)
        elif transaction_type=="withdraw":
            if account.withdraw(amount):
                self.transaction_history[account_id].append((transaction_type, amount))
                return "Transaction completed."
            else:
                return "Insufficient funds."
        else:
            return"Invalid transaction type."


    def  get_transaction_history(self,account_id):
        return self.transaction_history.get(account_id, [])

class BankAccount:
    def __init__(self,account_id, holder_name, balance):
        self.account_id=account_id
        self.holder_name=holder_name
        self.balance=balance

    def deposit(self, amount):
        if amount>0:
            self.balance+=amount

    def withdraw(self, amount):
        if 0<amount<=self.balance:
            self.balance-=amount
            return True
        return False

    def get_balance(self):
        return self.balance


def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')



def main():
    bank_name="-----------Bankof Python-----------"
    bank=Bank()

    while True:
        clear_screen()
        print(f"{bank_name}")
        print("PersonalBanking System")
        print("1. Create Account")
        print("2. Perform Transaction")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice=input("Enter your choice: ")

        if choice=="1":
            holder_name=input("Enter your name: ")
            initial_deposit=float(input("Enter initial deposit: "))
            account=bank.create_account(holder_name, initial_deposit)
            print(f"Account created successfully. Account Number: {account.account_id}")

        elif choice=="2":
            account_id=input("Enter Account Number: ")
            transaction_type=input("Enter transaction type (deposite/withdraw): ").lower()
            amount=float(input("Enter transaction amount: "))
            result=bank.perform_transaction(account_id, transaction_type, amount)
            print(result)

        elif choice=="3":
            account_id=input("Enter Account Number: ")
            account=bank.get_account(account_id)
            if account:
                print(f"Account Balance: ${account.get_balance()}")
            else:
                print("Account not found.")

        elif choice=="4":
            account_id=input("Enter Account Number: ")
            transactions=bank.get_transaction_history(account_id)
            if transactions:
                print("Transaction Hisotry: ")
                for trans_type, amount in transactions:
                    print(f"{trans_type.capitalize()}: ${amount}")
            else:
                print("Account not found or no transaction history.")

        elif choice=="5":
            print("Exiting the Python Banking System. GoodBye!")
            break

        else:
            print("Invalid choice. Please try again.")

        input("\n Press Enter to continue...")

if __name__=="__main__":
    main()





