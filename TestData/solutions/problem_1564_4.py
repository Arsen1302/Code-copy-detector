class Solution:
    def solution_1564_4(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        if ((rows + cols - 1) % 2 or grid[0][0] == ")"
                or grid[rows - 1][cols - 1] == "("):
            return False
        opened = [[set() for _ in range(cols)] for _ in range(rows)]
        opened[0][0].add(1)
        row = 0
        for col in range(1, cols):
            if grid[row][col] == "(":
                opened[row][col].update(n + 1 for n in opened[row][col - 1])
            else:
                opened[row][col].update(n - 1 for n in opened[row][col - 1]
                                        if n > 0)
        col = 0
        for row in range(1, rows):
            if grid[row][col] == "(":
                opened[row][col].update(n + 1 for n in opened[row - 1][col])
            else:
                opened[row][col].update(n - 1 for n in opened[row - 1][col]
                                        if n > 0)
        for row in range(1, rows):
            for col in range(1, cols):
                opened[row - 1][col].update(opened[row][col - 1])
                if grid[row][col] == "(":
                    opened[row][col].update(n + 1 for n in
                                            opened[row - 1][col])
                else:
                    opened[row][col].update(n - 1 for n in
                                            opened[row - 1][col] if n > 0)
        return 0 in opened[rows - 1][cols - 1]