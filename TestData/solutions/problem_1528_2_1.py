class Solution:
    def solution_1528_2_1(self, piles: List[List[int]], k: int) -> int:
        
        n = len(piles)
        cache = {}    # <--------------- Caching using dictionary

        def solution_1528_2_2(index, remain_k):
            
            if remain_k == 0:
                return 0
            if index == n:
                return 0
            if (index, remain_k) in cache:
                return cache[(index, remain_k)]

            ans = 0
            ans = max(ans, solution_1528_2_2(index+1, remain_k))
            running_prefix = 0
            for i in range(1, min(remain_k, len(piles[index]))+1):
                running_prefix += piles[index][i-1]
                ans = max(ans, running_prefix+solution_1528_2_2(index+1, remain_k-i))
            cache[(index, remain_k)] = ans
            return ans
        
        return solution_1528_2_2(0, k)