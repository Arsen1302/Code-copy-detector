class Solution:
    def solution_1470_4(self, questions: List[List[int]]) -> int:
        dp = [0 for _ in range(len(questions)+1)]
        
        for index, value in enumerate(questions):
            points, brainpower = value
            
            if brainpower + index + 1 < len(questions):
                dp[brainpower+index+1] = max(dp[brainpower+index+1], points+dp[index])
            else:
                dp[-1] = max(dp[-1], dp[index]+points)
            
            if index + 1 < len(questions):
                dp[index+1] = max(dp[index], dp[index+1])
                    
        return dp[-1]