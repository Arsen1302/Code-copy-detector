class Solution:
    def solution_466_4(self, nums: List[int]) -> bool:
        for i, a in enumerate(nums):
            if (abs(a - i) > 1):
                return False
        
        return True