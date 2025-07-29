class Solution:
    def solution_1469_4(self, target: int, maxDoubles: int) -> int:
        ans = 0 
        while target > 1 and maxDoubles: 
            ans += 1
            if target&amp;1: target -= 1
            else: 
                target //= 2
                maxDoubles -= 1
        return ans + target - 1