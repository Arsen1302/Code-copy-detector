class Solution:
    def solution_1625_4(self, grid: List[List[int]]) -> int:
        freq = Counter(tuple(row) for row in grid)
        return sum(freq[tuple(col)] for col in zip(*grid))