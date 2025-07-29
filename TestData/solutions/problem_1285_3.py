class Solution:
    def solution_1285_3(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            mat = [list(m[::-1]) for m in zip(*mat)]
        return False