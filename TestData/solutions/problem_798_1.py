class Solution:
    def solution_798_1(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        cost,start,ans = 0,0,0
        for i in range(n):
            diff = abs(ord(s[i]) - ord(t[i]))
            if cost + diff <= maxCost:
                # we can increase our sliding window
                cost += diff
            else:
                # we are unable to increase our sliding window
                ans = max(ans,i - start)
                while True:
                    cost -= abs(ord(s[start]) - ord(t[start]))
                    start += 1
                    if cost + diff <= maxCost: break
                if cost + diff > maxCost: start = i + 1
                else: cost += diff
                    
        ans = max(ans,n - start)
        return ans