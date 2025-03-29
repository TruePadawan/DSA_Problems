'''
Implement long multiplication
123 x 456
Loop through num2:
For ith num in num2:
    multiply it with the
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        table = []
        remainder = 0
        for i in range(len(num1)):
            int1 = int(num1[i])
            values = []
            
            j = len(num2) - 1
            while j > 0:
                int2 = int(num2[j])
                int1_x_2 = int1 * int2
                