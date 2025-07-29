class Solution:
    def solution_1405_3(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix = [0]
        stack = []
        upper = [-1]*len(s)
        lower = [-1]*len(s)
        lo = -1
        for i, ch in enumerate(s): 
            prefix.append(prefix[-1] + (ch == '*'))
            stack.append(i)
            if ch == '|': 
                while stack: upper[stack.pop()] = i 
                lo = i 
            lower[i] = lo 
        
        ans = []
        for x, y in queries: 
            lo = upper[x]
            hi = lower[y]
            if hi != -1 and lo != -1 and lo <= hi: ans.append(prefix[hi+1] - prefix[lo])
            else: ans.append(0)
        return ans