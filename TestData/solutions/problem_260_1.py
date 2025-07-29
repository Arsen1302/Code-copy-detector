class Solution:
    def solution_260_1(self, nums: List[int]) -> int:
        nums.sort()
        mid = nums[len(nums)//2]
        result = 0
        for i in nums:
            result+=abs(mid-i)
        return result