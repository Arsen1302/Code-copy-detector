class Solution:
    def solution_260_4(self, nums: List[int]) -> int:
        nums_two = sorted(nums)
        
        if len(nums_two) % 2 == 0:
            median = (nums_two[len(nums_two)//2] + nums_two[(len(nums_two)//2) - 1]) // 2
        else:
            median = nums_two[len(nums_two)//2]
        
        steps = 0
        
        for x in nums_two:
            if x != median:
                steps += abs(x-median)
        
        return steps