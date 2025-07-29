class Solution:
    def solution_826_5(self, grid: List[List[int]], k: int) -> List[List[int]]:
        for j in range(k):  # Shifting k times
            for i in range(len(grid)):  # Shifting without disturbing the structure
                if i==len(grid)-1:
                    a=grid[i].pop()
                    grid[0].insert(0,a)
                else:
                    a=grid[i].pop()
                    grid[i+1].insert(0,a)
        return grid