class Solution:
    def solution_208_4(self, n: int) -> int:
        ans = 0
        while n > 1:
            if n % 2:
                if n > 3 and n &amp; 1 == 1 and (n >> 1) &amp; 1 == 1:
                    n += 1
                else:
                    n -= 1
                ans += 1
            n //= 2
            ans += 1
        return ans