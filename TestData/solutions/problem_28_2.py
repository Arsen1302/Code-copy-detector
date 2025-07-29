class Solution:
    def solution_28_2(self, s: str, t: str) -> int:
        ## RC ##
		## APPROACH : DP ##
		## LOGIC ##
		#	1. Point to be noted, empty seq is also subsequence of any sequence i.e "", "" should return 1. so we fill the first row accordingly
		#	2. if chars match, we get the maximum of [diagonal + upper, upper + 1] (Try below example)
		#	3. if no match, we pull the upper value
		
        ## EXAMPLE : "axacccax" "aca"	##
		## STACK TRACE ##
        # [      ""  a  c  a
        #     "" [1, 0, 0, 0], 
        #     a  [1, 1, 0, 0], 
        #     x  [1, 1, 0, 0], 
        #     a  [1, 2, 0, 0], 
        #     c  [1, 2, 2, 0], 
        #     c  [1, 2, 4, 0], 
        #     c  [1, 2, 6, 0], 
        #     a  [1, 3, 6, 6], 
        # ]
        
		## TIME COMPLEXITY : O(MxN) ##
		## SPACE COMPLEXITY : O(MxN) ##

        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
        
        for k in range(len(dp)):
            dp[k][0] = 1
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if(s[i-1] == t[j-1] and dp[i-1][j-1]):
                    dp[i][j] = max(dp[i-1][j-1] + dp[i-1][j], dp[i-1][j]+1)
                else:
                    dp[i][j] = dp[i-1][j]
        # print(dp)
        return dp[-1][-1]