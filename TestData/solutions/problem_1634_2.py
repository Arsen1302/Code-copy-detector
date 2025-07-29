class Solution:
    def solution_1634_2(self, nums: List[int]) -> int:
        ans = 0 
        prev = 1_000_000_001
        for x in reversed(nums): 
            d = ceil(x/prev)
            ans += d-1
            prev = x//d
        return ans