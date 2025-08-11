from functools import reduce
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_groups = {}
        for word in strs:
            sorted_word = reduce(lambda x, y: x + y, sorted(word), "")
            if word_groups.get(sorted_word) is None:
                word_groups[sorted_word] = [word]
            else:
                word_groups[sorted_word].append(word)
        return list(word_groups.values())

a = ["neet","code","love","you"]
print(reduce(lambda x, y: x + "#" + y, a))
