class Solution:
    def solution_1431_5(self, nums: List[int]) -> int:
        minVal = min(nums)
        maxVal = max(nums)
        
        minIndex = nums.index(minVal)
        maxIndex = nums.index(maxVal)
        
        r1 = max(minIndex, maxIndex) + 1
        r2 = len(nums) - min(minIndex, maxIndex)
        r3 = min(minIndex, maxIndex) + 1 + len(nums) - max(minIndex, maxIndex)
        return min(r1,r2,r3)