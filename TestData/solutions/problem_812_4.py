class Solution:
    def solution_812_4(self, s: str) -> int:
        target = {}
        for c in s: target[c] = 1 + target.get(c, 0)
        for c in target: target[c] = max(0, target[c] - len(s)//4)
            
        freq = defaultdict(int)
        ans = len(s)
        ii = 0
        for i, c in enumerate(s): 
            freq[c] = 1 + freq.get(c, 0)
            while ii < len(s) and all(freq.get(x, 0) >= target[x] for x in target): 
                ans = min(ans, i-ii+1)
                freq[s[ii]] -= 1
                ii += 1
        return ans