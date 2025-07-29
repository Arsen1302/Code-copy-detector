class Solution:
    def solution_344_4_1(self, text1: str, text2: str) -> int:
        
        dp = {}
        n = len(text1)
        m = len(text2)
        
        def solution_344_4_2(i,j):
            if i< 0 or i>=n or j<0 or j>=m:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            result = -float("inf")
            if text1[i] == text2[j]:
                result = 1 + solution_344_4_2(i+1,j+1)
            else:
                result = max(solution_344_4_2(i,j+1), solution_344_4_2(i+1,j))
            dp[(i,j)] = result
            return result
        
        result = solution_344_4_2(0,0)
        
        return n-result + m-result