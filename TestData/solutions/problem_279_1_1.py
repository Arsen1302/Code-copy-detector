class Solution:
    def solution_279_1_1(self, nums: List[int]) -> bool:
        def solution_279_1_2(i, j):
            if i == j:
                return nums[i]
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            score = max(nums[j] - solution_279_1_2(i, j-1), nums[i] - solution_279_1_2(i+1, j))
            memo[(i, j)] = score
            
            return score
            
        memo = {}            
        return solution_279_1_2(0, len(nums)-1) >= 0