class Solution:
    def solution_1287_3_1(self, s: str) -> int:
        s = deque(int(x) for x in s)
        
        def solution_1287_3_2(s, val=0): 
            """Return min type-2 op to make s alternating."""
            ans = int(s[0] != val)
            for i in range(1, len(s)): 
                val ^= 1
                if val != s[i]: ans += 1
            return ans
        
        x0, x1 = solution_1287_3_2(s, 0), solution_1287_3_2(s, 1)
        ans = min(x0, x1)
        for _ in range(len(s)):
            if len(s)&amp;1: x0, x1 = x1 + s[0] - (s[0]^1), x0 - s[0] + (s[0]^1)
            else: x0, x1 = x1, x0
            s.append(s.popleft())
            ans = min(ans, x0, x1)
        return ans