from tabnanny import check
from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.bank = balance
        


    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # check account
        if check(account1) and check(account2):
            m1 = self.bank[account1 - 1]
            if m1 >= money:
                self.bank[account1 - 1] -= money
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if check(account):
            self.bank[account - 1] += money
            return True
        return False


    def withdraw(self, account: int, money: int) -> bool:
        if check(account):
            m = self.bank[account - 1]
            if m > money:
                self.bank[account - 1] -= money
                return True
        return False

    
    def check(self, account):
        return 1 <= account <= len(self.bank)



# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)