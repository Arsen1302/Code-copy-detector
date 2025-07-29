class Solution:
    def solution_65_4(self, nums: List[int]) -> int:
        totalMax = prevMax = prevMin = nums[0]
        for i,num in enumerate(nums[1:]):
            currentMin = min(num, prevMax*num, prevMin*num)
            currentMax = max(num, prevMax*num, prevMin*num)
            totalMax = max(currentMax, totalMax)
            prevMax = currentMax
            prevMin = currentMin
        return totalMax