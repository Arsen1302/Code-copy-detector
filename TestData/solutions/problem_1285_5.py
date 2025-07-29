class Solution:
    def solution_1285_5(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(3):
            if mat == target:
                return True
            mat = [list(x[::-1]) for x in zip(*mat)]
        return mat == target