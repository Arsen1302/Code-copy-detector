class Solution:
    def solution_338_4_1(self, mat):
        for row in mat:
            for cell in row:
                yield cell
    def solution_338_4_2(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        gen = self.solution_338_4_1(mat)
        return [[next(gen) for _ in range(c)] for _ in range(r)] if len(mat) * len(mat[0]) == r * c else mat