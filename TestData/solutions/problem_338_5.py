class Solution:
    def solution_338_5(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        gen = (cell for row in mat for cell in row)
        return [[next(gen) for _ in range(c)] for _ in range(r)] if len(mat) * len(mat[0]) == r * c else mat