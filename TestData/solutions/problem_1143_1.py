class Solution:
    def solution_1143_1(self, stones: List[int]) -> int:
        dp = [[0 for _ in range(len(stones))] for _ in range(len(stones))]     # dp table n x n
        run_sum = [0]                            # running sum -> sum [i..j] = run_sum[j] - run_sum[i]
        s = 0
        
		## Calculation of running sum
        for i in stones:
            s += i
            run_sum.append(s)
		
        n = len(stones) 
        
        for k in range(1, n):               # no. of stones left
            for i in range(0, n - k):   # from each starting point
                remove_i_stone = (run_sum[i+k+1] - run_sum[i+1])    # score after removing i th stone
                remove_j_stone = (run_sum[i+k] - run_sum[i])             # score after removing j th stone
                
                if (n-(k+1))%2 == 0:        # alice's move 
                    dp[i][i+k] = max(remove_i_stone + dp[i+1][i+k],
                                    remove_j_stone + dp[i][i+k-1])
                else:                       # bob's move
                    dp[i][i+k] = min(-remove_i_stone + dp[i+1][i+k],
                                    - remove_j_stone + dp[i][i+k-1])
                    
        return dp[0][n - 1]