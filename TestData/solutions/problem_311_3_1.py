class Solution:
    def solution_311_3_1(self, N: int) -> int:
        
        def solution_311_3_2(k):
            """Return number of beautiful arrangements."""
            if k == N: return 1 # boundary condition
            ans = 0
            for kk in range(k, N):
                if nums[kk] % (k+1) == 0 or (k+1) % nums[kk] == 0: 
                    nums[k], nums[kk] = nums[kk], nums[k]
                    ans += solution_311_3_2(k+1)
                    nums[k], nums[kk] = nums[kk], nums[k]
            return ans 
            
        nums = list(range(1, N+1))
        return solution_311_3_2(0)