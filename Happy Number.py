class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        repeats = {}
        nums = list(str(n))
        result = 0
        while result != 1:
            result = 0
            for num in nums:
                result += int(num) ** 2
            if repeats.get(result):
                return False
            repeats[result] = True
            nums = list(str(result))
        return True