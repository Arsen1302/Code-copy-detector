class Solution:
    def solution_501_4_1(self, A: List[int], K: int) -> float:
        prefix = [0]
        for x in A: prefix.append(prefix[-1] + x) # prefix sum 
        
        @lru_cache(None)
        def solution_501_4_2(i, k): 
            """Return largest sum of average of A[lo:hi+1] with at most k groups."""
            if i == 1 or k == 1: return prefix[i]/i # boundary condition 
            if i <= k: return prefix[i] # shortcut 
            ans = solution_501_4_2(i, k-1)
            for ii in range(1, i):
                ans = max(ans, solution_501_4_2(i-ii, k-1) + (prefix[i] - prefix[i-ii])/ii)
            return ans 
            
        return solution_501_4_2(len(A), K)