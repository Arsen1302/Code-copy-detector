class Solution:
    def solution_530_3_1(self, s: str) -> bool:
        def solution_530_3_2(i, ans):
            if i>=len(s):
                return len(ans)>1           
            n = 0
            for j in range(i, len(s)):
                n = n*10 + int(s[j]) 
                if len(ans)<1 or (ans[-1]-1==n):
                    ans.append(n)
                    if solution_530_3_2(j+1, ans):
                        return True
                    ans.pop()
        
        return solution_530_3_2(0, [])