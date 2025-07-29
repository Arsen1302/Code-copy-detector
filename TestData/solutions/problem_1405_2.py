class Solution:
    def solution_1405_2(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix = [0]
        candles = []
        for i, ch in enumerate(s): 
            if ch == '|': candles.append(i)
            if ch == '|': prefix.append(prefix[-1])
            else: prefix.append(prefix[-1] + 1)
        
        ans = []
        for x, y in queries: 
            lo = bisect_left(candles, x)
            hi = bisect_right(candles, y) - 1
            if 0 <= hi and lo < len(candles) and lo <= hi: 
                ans.append(prefix[candles[hi]+1] - prefix[candles[lo]])
            else: ans.append(0)
        return ans