class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        tape = ""
        for char in s:
            if char.isdigit() is not True:
                tape += char
            else:
                multiply_by = int(char)
                tape *= multiply_by
            if len(tape) >= k:
                return tape[k-1]