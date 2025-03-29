from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            divisible_by_3 = i % 3 == 0
            divisible_by_5 = i % 5 == 0
            if divisible_by_3 and divisible_by_5:
                result.append("FizzBuzz")
            elif divisible_by_3:
                result.append("Fizz")
            elif divisible_by_5:
                result.append("Buzz")
            else:
                result.append(f"{i}")
        return result
