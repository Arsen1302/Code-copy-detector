class Solution:
    def solution_1407_3(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            if i%10==nums[i]:
                return i
        return -1