class Solution:
    def solution_248_2(self, nums: List[int]) -> List[int]:                        
        result = [i for i in range(0, len(nums)+1)] # build an array (0, 1, 2, 3, ..., n)
        for i in nums: result[i] = 0 # we index this array, setting "found" elements to zero
        return [i for i in result if i != 0] # we return results that aren't zero