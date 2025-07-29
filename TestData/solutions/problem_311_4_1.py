class Solution:
    def solution_311_4_1(self, N: int) -> int:
        
        def solution_311_4_2(k):
            """Return number of beautiful arrangements."""
            if k == 1: return 1 # boundary condition 
            ans = 0
            for kk in range(k):
                if nums[kk] % k == 0 or k % nums[kk] == 0: 
                    nums[k-1], nums[kk] = nums[kk], nums[k-1]
                    ans += solution_311_4_2(k-1)
                    nums[k-1], nums[kk] = nums[kk], nums[k-1]
            return ans 
            
        nums = list(range(1, N+1))
        return solution_311_4_2(N)