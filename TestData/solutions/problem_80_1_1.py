class Solution:
    def solution_80_1_1(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        @cache
        def solution_80_1_2(i, j):
            """Return min health at (i,j)."""
            if i == m or j == n: return inf
            if i == m-1 and j == n-1: return max(1, 1 - dungeon[i][j])
            return max(1, min(solution_80_1_2(i+1, j), solution_80_1_2(i, j+1)) - dungeon[i][j])
        
        return solution_80_1_2(0, 0)