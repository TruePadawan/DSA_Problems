from functools import reduce
from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "#"
        return reduce(lambda x, y: x + "]" + y, strs)

    def decode(self, s: str) -> List[str]:
        if s == "#":
            return []
        return s.split("]")
