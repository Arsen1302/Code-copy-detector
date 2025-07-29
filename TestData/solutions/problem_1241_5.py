class Solution:
    def solution_1241_5(self, A: List[int]) -> int:
                        
		# Because we also "look ahead", we want to shorten the DP array
        N = len(A) - 1
            
        dp = [
            [float('inf')] * 3
            for _ in range(N)
        ]
        
		# Initial state
        dp[0] = [1, 0, 1]
        
        for i in range(1, N):
            for j in range(3):
            
                """
				This line here is the tricky one.
				Think about this: if we can jump to a space but the immediate next space is a rock,
				can will we succeed? NO. We don't! So we must consider this
				"""
                if A[i] == j+1 or A[i+1] == j+1:
                    dp[i][j] = float('inf')
                else:
					"""
					Other people use the modulo "%" to be a bit more clean,
					but to me, this is the easiest to read :)
					"""
                    dp[i][j] = min([
                        dp[i-1][0] + (1 if j != 0 else 0),
                        dp[i-1][1] + (1 if j != 1 else 0),
                        dp[i-1][2] + (1 if j != 2 else 0),
                    ])
                    
        return min(dp[-1])