class Solution:
    def solution_1077_3_1(self, s: str) -> int:
        
        def solution_1077_3_2(i, seen=set()):
            """Find max length via backtracking."""
            ans = 0
            if i < len(s): # boundary condition when i == len(s)
                for ii in range(i+1, len(s)+1): 
                    if s[i:ii] not in seen: 
                        seen.add(s[i:ii])
                        ans = max(ans, 1 + solution_1077_3_2(ii, seen))
                        seen.remove(s[i:ii])
            return ans 
            
        return solution_1077_3_2(0)