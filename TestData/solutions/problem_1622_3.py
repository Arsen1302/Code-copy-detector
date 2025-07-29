class Solution:
    def solution_1622_3(self, nums: List[int]) -> int:
        ans = 0
        l = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                ans += i - l + 1
            else:
                l = i + 1
        
        return ans