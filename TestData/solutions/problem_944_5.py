class Solution:
    def solution_944_5(self, nums: List[int]) -> int:
        startValue = x = 1
        for num in nums:
            x += num
            if x < 1:
                startValue += 1 - x
                x = 1
        return startValue