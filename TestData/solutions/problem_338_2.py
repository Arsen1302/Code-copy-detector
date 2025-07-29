class Solution:
    def solution_338_2(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        queue = [cell for row in mat for cell in row] if r*c==len(mat)*len(mat[0]) else []
        return [[queue.pop(0) for _ in range(c)] for _ in range(r)] if queue else mat