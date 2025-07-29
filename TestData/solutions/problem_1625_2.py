class Solution:
    """
    Time:   O(n^3)
    Memory: O(1)
    """

    def solution_1625_2(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pairs = 0

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if grid[i][k] != grid[k][j]:
                        break
                else:
                    pairs += 1

        return pairs