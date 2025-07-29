class Solution:
    def solution_319_3(self, nums: List[int]) -> int:
        for i in range(0, len(nums)-1, 2):  # pairwise comparison
            if nums[i] != nums[i+1]:  # found the single element
                return nums[i]
        return nums[-1]  # the last element is the single element