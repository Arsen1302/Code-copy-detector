class Solution:
    def solution_1239_3_1(self, nums: List[int]) -> int:
        
        def solution_1239_3_2(x):
            return 1 if x > 0 else -1 if x < 0 else 0
        
        return solution_1239_3_2(math.prod(nums))