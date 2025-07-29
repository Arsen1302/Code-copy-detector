class Solution:
    def solution_1377_4(self, nums: List[int]) -> int:
        my_max = -1
        min_here = math.inf # the minimum element until i-th position
        for i in range(len(nums)):
            if min_here > nums[i]:
                min_here = nums[i]
            dif = nums[i] - min_here 
            if my_max < dif and dif != 0: # the difference mustn't be 0 because nums[i] < nums[j] so they can't be equals
                my_max = dif
        return my_max