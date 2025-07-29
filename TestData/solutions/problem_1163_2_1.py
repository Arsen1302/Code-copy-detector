class Solution:
    def solution_1163_2_1(self, n: int) -> List[int]:
        ans = [0]*(2*n-1)
        
        def solution_1163_2_2(i): 
            """Return largest sequence after filling in ith position."""
            if i == 2*n-1 or ans[i] and solution_1163_2_2(i+1): return True 
            for x in reversed(range(1, n+1)): 
                if x not in ans: 
                    ii = x if x > 1 else 0 
                    if i+ii < 2*n-1 and ans[i] == ans[i+ii] == 0: 
                        ans[i] = ans[i+ii] = x
                        if solution_1163_2_2(i+1): return True 
                        ans[i] = ans[i+ii] = 0 
        
        solution_1163_2_2(0)
        return ans