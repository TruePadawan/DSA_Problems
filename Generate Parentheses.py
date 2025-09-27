from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        valid_parens = []
        paren_len = n * 2
        def recursive_sol(available_parens: dict[str, int], current_paren: str):
            # Automatically invalid if we've used more closing than opening brace
            auto_invalid = available_parens[")"] < available_parens["("]
            if auto_invalid:
                return
            is_valid = len(current_paren) == paren_len and available_parens["("] == 0 and available_parens[")"] == 0
            if is_valid:
                valid_parens.append(current_paren)
    
            opening_count = available_parens["("]
            closing_count = available_parens[")"]
    
            if opening_count > 0:
                recursive_sol({"(": opening_count - 1, ")": closing_count}, current_paren + "(")
    
            if closing_count > 0:
                recursive_sol({"(": opening_count, ")": closing_count - 1}, current_paren + ")")
        parens = {"(": n-1, ")": n}
        recursive_sol(parens, "(")
        return valid_parens

    

soln = Solution()
print(soln.generateParenthesis(0))