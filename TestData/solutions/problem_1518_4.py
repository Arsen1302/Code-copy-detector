class Solution:
    def solution_1518_4(self, nums: List[int]) -> bool:

        nums.sort()

        pairs = len(nums) // 2

        for i in range(0,len(nums)-1,2):
            if nums[i] != nums[i+1]:
                return False

        return True