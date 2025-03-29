from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid_transactions = set()
        # Convert the transactions into a hash table
        transaction_table = {}
        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            parsedTime = int(time)
            parsedAmount = int(amount)

            if transaction_table.get(name) is None:
                transaction_table[name] = [
                    {
                        "time": parsedTime,
                        "amount": parsedAmount,
                        "city": city,
                        "raw": transaction,
                    }
                ]
                if parsedAmount > 1000:
                    invalid_transactions.add(transaction)
            else:
                prevTransaction = transaction_table[name][-1]
                timeDiff = parsedTime - prevTransaction["time"]
                if timeDiff <= 60:
                    invalid_transactions.add(transaction)
                # Add the previous transaction if it's not there already and the current transaction doesn't exceed 1000
                # It won't be there if its amount doesn't exceed 1000
                if prevTransaction["amount"] <= 1000 and parsedAmount <= 1000:
                    invalid_transactions.add(prevTransaction["raw"])
                transaction_table[name].append(
                    {
                        "time": parsedTime,
                        "amount": parsedAmount,
                        "city": city,
                        "raw": transaction,
                    }
                )
        return list(invalid_transactions)

