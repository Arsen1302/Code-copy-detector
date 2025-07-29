class Solution:
    def solution_284_4_1(self, nums: List[int], S: int) -> int:
        nums = [0]+nums
        @lru_cache(None)
        def solution_284_4_2(i, total):
            if i == 0: return total == 0
            return solution_284_4_2(i-1, total - nums[i]) + solution_284_4_2(i-1, total + nums[i])
            
        return solution_284_4_2(len(nums)-1, S)