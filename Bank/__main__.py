from bank import Bank
from rich import print
from pwinput import pwinput


def main():


        print(f"-=-=-=-= BANK -=-=-=-=")
        name = input("Type you name: ")
        id = input("Type your id: ")
        key = pwinput("Type in your password: ")
        user = Bank(name,id,key)
        while True:
            print(f"-=-=-=-= BANK -=-=-=-=")
            print("Select one of the following options!\n1 - Deposit\n2 - Withdraw\n3 - See your balance\n0 - Leave")
            print("-=-=-=-=-=-=-=-=-=-=-=-=")
            choice = int(input("Your choice: "))
            if choice == 1:
                try:
                    money = float(input("How much money do you wanna deposit?: USD $"))
                    user.deposit(money)
                except ValueError:
                    print("[red]ERROR! Invalid value!")
                except TypeError:
                    print("[red]ERROR! Invalid Type!")
            elif choice == 2:
                try:
                    money = float(input("How much money do you wanna withdraw?: USD $"))
                    user.withdraw(money)
                except PermissionError as  e:
                    print(e)
                except ValueError as e:
                    print(e)
                except TypeError as e:
                    print(e)
            elif choice == 3:
                try:
                    print(user.balance)
                except PermissionError as e:
                    print(e)
            else:
                if choice == 0:
                    print("Thanks for Visiting our bank! Have a good day :)")
                    break


if __name__ == "__main__":
    main()