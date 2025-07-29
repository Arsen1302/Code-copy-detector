class Solution:
    def solution_1595_1(self, num: int, k: int) -> int:
        
        if num == 0:
            return 0
        
        if num < k:
            return -1
        
        if num == k:
            return 1
        
        ans = -1
        i = 1

        while i <= 10:
            if (num - i * k) % 10 == 0 and i * k <= num:
                return i
            i += 1

        return ans