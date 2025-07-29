class Solution:
    def solution_516_5(self, s: str) -> int:
        locs = [[-1] for _ in range(26)]
        for i, x in enumerate(s): locs[ord(x)-65].append(i)
        
        ans = 0 
        for i in range(26): 
            locs[i].append(len(s))
            for k in range(1, len(locs[i])-1): 
                ans += (locs[i][k] - locs[i][k-1]) * (locs[i][k+1] - locs[i][k])
        return ans