class Solution:
    def solution_1358_4_1(self, tasks: List[int], sessionTime: int) -> int:
        
        @cache
        def solution_1358_4_2(mask, rem):
            """Return minimum work sessions to finish tasks indicated by set bits in mask."""
            if not mask: return 0 # done 
            ans = inf 
            for i, x in enumerate(tasks): 
                if mask &amp; (1<<i): 
                    if x <= rem: ans = min(ans, solution_1358_4_2(mask ^ (1<<i), rem - x))
                    else: ans = min(ans, 1 + solution_1358_4_2(mask ^ (1<<i), sessionTime - x))
            return ans
        
        return solution_1358_4_2((1<<len(tasks))-1, 0)