class Solution:
    def solution_709_4_1(self, costs: List[List[int]]) -> int:
        
        @lru_cache(None)
        def solution_709_4_2(i, j): 
            if i == 0 and j == 0: return 0
            if j == 0: return solution_709_4_2(i-1, 0) + costs[i-1][0]
            if i == 0: return solution_709_4_2(0, j-1) + costs[j-1][1]
            return min(solution_709_4_2(i-1, j) + costs[i+j-1][0], solution_709_4_2(i, j-1) + costs[i+j-1][1])
        
        return solution_709_4_2(len(costs)//2, len(costs)//2)