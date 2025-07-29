class Solution:
    def solution_1490_1(self, num1: int, num2: int) -> int:
        ans = 0 
        while num1 and num2: 
            ans += num1//num2
            num1, num2 = num2, num1%num2
        return ans