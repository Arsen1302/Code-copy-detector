class Solution:
    def solution_1263_4_1(self, nums):
        N = len(nums)
        solution_1263_4_1 = [(0, 0) for _ in range(N)]
        ans = 0
        
        for x in range(N):
            for y in range(x, N):
                if x == y:
                    solution_1263_4_1[y] = (nums[y], nums[y])
                else:
                    solution_1263_4_1[y] = (min(solution_1263_4_1[y-1][0], nums[y]), solution_1263_4_1[y-1][1] + nums[y])
                    a,b = solution_1263_4_1[y]
                    ans = max(ans, a*b)
        
        return ans%(10**9+7)
    def solution_1263_4_2(self, nums):
        # Just to flush out the stack at the end of iterations.
        nums.append(0)
        
        N = len(nums)
        z = 0

        S = deque([[nums[0], 0]])
        
        rolling_sum = [0]*N
        rolling_sum[0] = nums[0]

        for idx in range(1, N):
            n = nums[idx]

            while S and S[-1][0] > n:                
                a,b = S.pop()
                
                if S:
                    b = S[-1][1]+1
                    z = max(z, rolling_sum[idx-1]*S[0][0])
                                    
                z = max(z, (rolling_sum[idx-1] - rolling_sum[b-1]) * a)

            S.append([nums[idx], idx])
            rolling_sum[idx] = n + rolling_sum[idx-1]
        return z%(10**9+7)
                
    def solution_1263_4_3(self, nums: List[int]) -> int:
        return self.solution_1263_4_2(nums)