from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
    

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        acct1_index = account1 - 1
        acct2_index = account2 - 1

        # The account doesn't exist
        if acct1_index >= len(self.balance) or acct2_index >= len(self.balance):
            return False
        
        # Not enough balance
        if self.balance[acct1_index] < money:
            return False
        
        self.balance[acct2_index] += money
        self.balance[acct1_index] -= money
        return True

        

    def deposit(self, account: int, money: int) -> bool:
        acct_index = account - 1

        # The account doesn't exist
        if acct_index >= len(self.balance):
            return False

        self.balance[acct_index] += money
        return True
        

    def withdraw(self, account: int, money: int) -> bool:
        acct_index = account - 1

        # The account doesn't exist
        if acct_index >= len(self.balance):
            return False
        
        # Not enough balance
        if self.balance[acct_index] < money:
            return False

        self.balance[acct_index] -= money
        return True       


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)