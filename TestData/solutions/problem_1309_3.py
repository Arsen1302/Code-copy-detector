class Solution:
    def solution_1309_3(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range (0,len(nums)):
            arr.append(nums[nums[i]])
        return arr