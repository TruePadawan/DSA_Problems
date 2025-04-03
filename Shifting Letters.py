import math
from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        alphabet_to_index = self.alphabet_to_index_dict()
        index_to_alphabet = list(alphabet_to_index.keys())
        increment = 0
        shifted_letters = ""
        for i in reversed(range(len(shifts))):
            char = s[i]
            increment += shifts[i]
            shifted_index = alphabet_to_index[char] + self.get_actual_index(increment)
            shifted_index = self.get_actual_index(shifted_index)
            shifted_letters += index_to_alphabet[shifted_index-1]
        return shifted_letters[::-1]

    def alphabet_to_index_dict(self):
        alphabet_dict = {}
        for i in range(26):
            alphabet_dict[chr(ord('a') + i)] = i + 1
        return alphabet_dict
    def get_actual_index(self, index: int):
        if index <= 26:
            return index
        while index > 26:
            index %= 26
        return index
soln = Solution()
print(soln.shiftingLetters("b", [26]))