class Solution:
    def solution_190_3_1(self, nums: List[int]) -> int:
        
        dp = {}
        result = [0]
        
        def solution_190_3_2(diff):
            if diff < 0:
                return "N"
            if diff > 0:
                return "P"
            return "E"
        
        def solution_190_3_3(index,sign):
            if index >= len(nums) - 1:
                return 1
            if index in dp:
                return dp[index]
            consider = 0
            dontConsider = 0
            x = solution_190_3_2(nums[index] - nums[index+1])
            if not sign and x!="E":
                consider = 1 + solution_190_3_3(index+1, x)
            elif sign == "P" and x == "N":
                consider = 1 + solution_190_3_3(index+1, x)
            elif sign == "N" and x == "P":
                consider = 1 + solution_190_3_3(index+1, x)
            dontConsider = solution_190_3_3(index+1,sign)
            
            dp[index] = max(consider, dontConsider)
            result[0] = max(result[0], dp[index])
            return dp[index]       
                
        solution_190_3_3(0,"")
        if result[0] == 0 and len(dp)==0:
            return len(nums)
        return result[0]