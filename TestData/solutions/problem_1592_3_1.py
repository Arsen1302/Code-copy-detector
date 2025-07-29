class Solution:
    def solution_1592_3_1(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        
        @cache
        def solution_1592_3_2(mask, k):
            """Return min unfairness of distributing cookies marked by mask to k children."""
            if mask == 0: return 0 
            if k == 0: return inf
            ans = inf 
            orig = mask 
            while mask: 
                mask = orig &amp; (mask - 1)
                amt = sum(cookies[i] for i in range(n) if (orig ^ mask) &amp; 1<<i)
                ans = min(ans, max(amt, solution_1592_3_2(mask, k-1)))
            return ans 
        
        return solution_1592_3_2((1<<n)-1, k)