class Solution:
    def solution_676_2_1(self, nums: List[int]) -> int:
        
        @cache
        def solution_676_2_2(v, mask): 
            """Return squareful arrays given prev value and mask."""
            if not mask: return 1 
            ans = 0 
            seen = set()
            for i, x in enumerate(nums): 
                if x not in seen and (mask == (1 << len(nums)) - 1 or mask &amp; (1 << i) and int(sqrt(x+v))**2 == x+v): 
                    seen.add(x)
                    ans += solution_676_2_2(x, mask ^ (1 << i))
            return ans 
        
        return solution_676_2_2(-1, (1 << len(nums)) - 1)