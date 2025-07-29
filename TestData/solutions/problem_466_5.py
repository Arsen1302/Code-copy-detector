class Solution:
    def solution_466_5(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[i]-i) > 1:
                return False
        return True