class Solution:
    def solution_1199_5(self, isWater: List[List[int]]) -> List[List[int]]:
        land = set()
        water = set()
        for r, row in enumerate(isWater):
            for c, v in enumerate(row):
                if v:
                    water.add((r, c))
                else:
                    land.add((r, c))
        height = 0
        cells = water
        while cells:
            new_cells = set()
            for r, c in cells:
                isWater[r][c] = height
                for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_cell = (r + i, c + j)
                    if new_cell in land:
                        land.remove(new_cell)
                        new_cells.add(new_cell)
            cells = new_cells
            height += 1
        return isWater