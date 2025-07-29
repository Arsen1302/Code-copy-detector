class Solution:
    def solution_1051_5(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)): 
            if nums[i] &amp; 1: 
                nums[i] -= 1
                ans += 1
        return ans if all(x == 0 for x in nums) else ans + 1 + self.solution_1051_5([x//2 for x in nums])