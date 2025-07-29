class Solution:
    def solution_1635_1(self, nums: List[int], diff: int) -> int:
        
        ans = 0
        n = len(nums)
        for i in range(n):
            if nums[i] + diff in nums and nums[i] + 2 * diff in nums:
                ans += 1
        
        return ans