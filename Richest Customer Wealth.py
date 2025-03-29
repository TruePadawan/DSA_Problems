from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for account_list in accounts:
            wealth_sum = 0
            for bank_balance in account_list:
                wealth_sum += bank_balance
            if wealth_sum > max_wealth:
                max_wealth = wealth_sum
        return max_wealth
