class Solution:
    def solution_1694_2(self, nums: List[int]) -> int:
        nums=sorted(nums,reverse=True)
        s=set(nums)
        for i in range(len(nums)):
            if 0-nums[i] in s:
                return nums[i]
        return -1