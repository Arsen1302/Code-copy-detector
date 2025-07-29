class Solution:
    def solution_815_2_1(self, n: int, start: int) -> List[int]:
        ans = [start]
        seen = set(ans)
        
        def solution_815_2_2(i, x): 
            """Return circular permutation with x at i."""
            if i == 2**n: 
                diff = ans[-1] ^ start
                if not diff &amp; (diff-1): return ans 
            for k in range(n): 
                xx = x ^ 1 << k 
                if xx not in seen: 
                    seen.add(xx)
                    ans.append(xx)
                    if tmp := solution_815_2_2(i+1, xx): return tmp 
                    ans.pop()
                    seen.remove(xx)
        
        return solution_815_2_2(1, start)