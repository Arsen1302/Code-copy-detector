class Solution:
    @lru_cache(None)
    def solution_405_5(self, n, k, row, column):
        if row < 0 or row > n-1 or column < 0 or column > n-1:
            return 0

        if k == 0:
            return 1

        directions = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

        total = 0

        for d in directions:
            total += (1/8)*self.solution_405_5(n,k-1,row+d[0],column+d[1])

        return total