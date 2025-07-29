class Solution:
    def solution_1490_3(self, num1: int, num2: int) -> int:
        ans = 0
        if num1 < num2:
            num1, num2 = num2, num1
        while num2:
            num1, num2 = num2, num1 - num2
            if num1 < num2:
                num1, num2 = num2, num1
            ans += 1
        return ans