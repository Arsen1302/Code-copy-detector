class Solution:
    def solution_191_5_1(self, nums: List[int], target: int) -> int:
        
        @cache
        def solution_191_5_2(n): 
            """Return number of combinations adding up to n."""
            if n <= 0: return int(n == 0)
            return sum(solution_191_5_2(n - x) for x in nums)
        
        return solution_191_5_2(target)