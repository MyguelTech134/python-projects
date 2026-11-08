from hashlib import sha256
from rich import print
class Bank:
    def __init__(self, name:str, id:str, key:str):
        self._name = name
        self.__id = id
        self.__balance = 0
        self.__hash = None

        if isinstance(key, str) and len(key) > 4:
            self.__hash = sha256(key.encode()).hexdigest()

    @property
    def balance(self):
        if self.get_key():
            return f"Your actual balance is: USD ${self.__balance}"
        else:
            raise PermissionError("[red]ERROR! Passwort invalid or incorrect![/]")

    @balance.setter
    def balance(self,value):
        raise PermissionError("You are not authorized to do that !")

    def get_key(self):
        from pwinput import pwinput
        user = pwinput("Type your password: ")
        hash = sha256(user.encode()).hexdigest()
        if self.verify_key(hash):
            return True
        raise PermissionError("[red]ERROR! Password is wrong!")

    def verify_key(self, key):
        if isinstance(key, str):
            if key == self.__hash:
                return True
            return False
        return False


    def deposit(self, money:float):
        if money < 0 or money == 0:
            print("[red]ERROR! Cant deposit a negative number or USD $0 ")
        else:
            self.__balance += money
            print(f"Deposit for USD ${money} Sucessfully! your actual balance is USD ${self.__balance:,.2f}")


    def withdraw(self,money):
        if money < 0 or money == 0:
            print("[red]ERROR! Cant withdraw a negative number or USD $0 ")
        elif money > self.__balance:
            print("[red]ERROR! You dont have enough money on you balance to withdraw that amount!")
        else:
            if self.get_key() and money <= self.__balance:
                self.__balance -= money
                print(f"Withdraw for USD ${money} sucessfully! your actual balance is: USD ${self.__balance:,.2f} ")

