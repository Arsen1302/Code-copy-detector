class Solution:
    def solution_812_5(self, s: str) -> int:
        freq = {}
        for c in s: freq[c] = 1 + freq.get(c, 0)
            
        ans = len(s)
        ii = 0
        for i, c in enumerate(s): 
            freq[c] -= 1
            while ii < len(s) and all(freq[x] <= len(s)//4 for x in freq): 
                ans = min(ans, i-ii+1)
                freq[s[ii]] += 1
                ii += 1
        return ans