class Solution:
    def solution_279_5_1(self, nums: List[int]) -> bool:
        
        @functools.lru_cache(maxsize=None)
        def solution_279_5_2(i, j):
            if i > j: return 0
            return max(
                nums[i] - solution_279_5_2(i+1, j),
                nums[j] - solution_279_5_2(i, j-1)
            )
        
        return solution_279_5_2(0, len(nums)-1) >= 0