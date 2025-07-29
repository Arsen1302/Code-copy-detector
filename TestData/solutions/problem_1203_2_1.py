class Solution:
    def solution_1203_2_1(self, nums: List[int], multipliers: List[int]) -> int:
        
        @lru_cache(2000)
        def solution_1203_2_2(lo, hi, k):
            """Return max score from nums[lo:hi+1]."""
            if k == len(multipliers): return 0
            return max(nums[lo] * multipliers[k] + solution_1203_2_2(lo+1, hi, k+1), nums[hi] * multipliers[k] + solution_1203_2_2(lo, hi-1, k+1))
        
        return solution_1203_2_2(0, len(nums)-1, 0)