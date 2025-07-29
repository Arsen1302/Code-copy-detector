class Solution:
    def solution_271_1(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            zero = one = 0
            mask = 1 << i
            for num in nums:
                if mask &amp; num: one += 1
                else: zero += 1    
            ans += one * zero        
        return ans