class Solution:
    def solution_398_2_1(self, forest: List[List[int]]) -> int:
        forest.append([0] * len(forest[0]))
        for row in forest: row.append(0)
        # solution_398_2_2
        def solution_398_2_2(i, j, I, J):
            manhattan = abs(i - I) + abs(j - J)
            detour = 0
            good, bad = [(i, j)], []
            visited = set()
            while True:
                if not good:
                    good, bad = bad, []
                    detour += 1
                i, j = good.pop()
                if i == I and j == J: return manhattan + detour * 2
                if (i, j) in visited: continue
                visited.add((i, j))
                for i, j, closer in ((i-1, j, i > I), (i+1, j, i < I), (i, j+1, j < J), (i, j-1, j > J)):
                    if forest[i][j]:
                        (good if closer else bad).append((i, j))
                    
        trees = [(height, r, c) for r, row in enumerate(forest) for c, height in enumerate(row) if forest[r][c] > 1]
        # check
        queue = [(0, 0)]
        reached = set()
        reached.add((0, 0))
        while queue:
            r, c = queue.pop()
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                row, col = r + dr, c + dc
                if forest[row][col] and (row, col) not in reached:
                    queue.append((row, col))
                    reached.add((row,col))
        if not all([(i, j) in reached for (height, i, j) in trees]): return -1
        trees.sort()
        return sum([solution_398_2_2(i, j, I, J) for (_, i, j), (_, I, J) in zip([(0, 0, 0)] + trees, trees)])