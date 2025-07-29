class Solution:
    def solution_1269_1(self, nums: List[int]) -> int:
        ans = 0
        for mask in range(1 << len(nums)): 
            val = 0
            for i in range(len(nums)): 
                if mask &amp; 1 << i: val ^= nums[i]
            ans += val
        return ans