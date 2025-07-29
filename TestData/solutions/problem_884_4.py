class Solution:
    def solution_884_4(self, mat: List[List[int]], k: int) -> List[int]:
        matIndexAndSumRow = [[sum(val),idx] for idx,val in enumerate(mat)]
        matIndexAndSumRow.sort()
        return [matIndexAndSumRow[i][-1] for i in range(k)]