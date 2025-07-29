class Solution:
    def solution_52_4_1(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = {}
        
        def solution_52_4_2(s,index):
            if not s:
                return True
            if index in dp:
                return dp[index]

            for i in range(len(s)+1):
                k = s[:i]
                if k in wordDict:
                    if solution_52_4_2(s[i:],index+i):
                        dp[index] = True
                        return dp[index]
            dp[index] = False
            return dp[index]
            
        return solution_52_4_2(s,0)