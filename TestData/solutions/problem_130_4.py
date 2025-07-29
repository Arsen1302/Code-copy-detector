class Solution:
    def solution_130_4(self, nums: List[int]) -> List[int]:
        val = 0
        for x in nums: val ^= x
        
        val &amp;= -val 
        ans = [0, 0]
        for x in nums: 
            if x&amp;val: ans[0] ^= x
            else: ans[1] ^= x
        return ans