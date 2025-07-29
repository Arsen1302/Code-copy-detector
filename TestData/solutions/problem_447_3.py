class Solution:
    def solution_447_3(self, nums: List[int]) -> int:
        ind = nums.index(max(nums))
        nums.sort()
        if 2*nums[-2] <= nums[-1]:
            return ind
   
        return -1