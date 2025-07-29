class Solution:
    def solution_984_3(self, nums: List[int]) -> int:
        
        x = max(nums)
        nums.remove(x)
        y = max(nums)
        
        return (x - 1) * (y - 1)