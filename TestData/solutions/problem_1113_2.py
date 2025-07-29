class Solution:
    def solution_1113_2(self, s: str) -> int:
        freq = {} # frequency table 
        for c in s: freq[c] = 1 + freq.get(c, 0)
        
        ans = 0
        seen = set()
        for k in freq.values(): 
            while k in seen: 
                k -= 1 
                ans += 1
            if k: seen.add(k)
        return ans