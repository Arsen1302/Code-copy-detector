class Solution:
    def solution_1397_1_1(self, nums: List[int]) -> int:
        target = reduce(or_, nums)
        
        @cache
        def solution_1397_1_2(i, mask): 
            """Return number of subsets to get target."""
            if mask == target: return 2**(len(nums)-i)
            if i == len(nums): return 0 
            return solution_1397_1_2(i+1, mask | nums[i]) + solution_1397_1_2(i+1, mask)
        
        return solution_1397_1_2(0, 0)