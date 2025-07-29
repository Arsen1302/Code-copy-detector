class Solution:
    def solution_1077_2_1(self, s: str) -> int:
        
        def solution_1077_2_2(i):
            """Find max length via backtracking."""
            nonlocal ans 
            if i == len(s): return (ans := max(ans, len(tabu)))
            for ii in range(i+1, len(s)+1): 
                if s[i:ii] not in tabu: 
                    tabu.add(s[i:ii])
                    solution_1077_2_2(ii)
                    tabu.remove(s[i:ii])
            
        ans = 1
        tabu = set()
        solution_1077_2_2(0)
        return ans