class Solution:
    def solution_1591_5_1(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        floor = len(grid) - 1
        memo = {}

        def solution_1591_5_2(node, level):
            key = (node, level)
            if key in memo:
                return memo[key]
            if level == floor:
                return node

            min_path = float('inf')
            for i, next_node in enumerate(grid[level + 1]):
                path = solution_1591_5_2(next_node, level + 1) + moveCost[node][i]
                min_path = min(min_path, path)

            memo[key] = min_path + node
            return memo[key]

        result = float('inf')
        for node in grid[0]:
            result = min(result, solution_1591_5_2(node, 0))

        return result