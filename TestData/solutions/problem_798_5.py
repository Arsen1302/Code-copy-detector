class Solution:
    def solution_798_5(self, s: str, t: str, maxCost: int) -> int:
        ans = ii = val = 0 
        for i in range(len(s)): 
            val += abs(ord(s[i]) - ord(t[i]))
            while ii <= i and val > maxCost: 
                val -= abs(ord(s[ii]) - ord(t[ii]))
                ii += 1
            ans = max(ans, i - ii + 1)
        return ans