class Solution:
    def solution_130_3(self, nums: List[int]) -> List[int]:
        diff = reduce(xor, nums)
        diff &amp;= -diff #retain last set bit 
        
        ans = [0]*2 
        for x in nums: ans[bool(diff &amp; x)] ^= x
        return ans