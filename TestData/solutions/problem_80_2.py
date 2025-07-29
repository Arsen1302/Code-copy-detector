class Solution:
    def solution_80_2(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        ans = [inf]*(n-1) + [1, inf]
        for i in reversed(range(m)): 
            for j in reversed(range(n)): 
                ans[j] = max(1, min(ans[j], ans[j+1]) - dungeon[i][j])
        return ans[0]