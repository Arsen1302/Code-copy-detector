class Solution:
    def solution_192_5(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        for i in range(min(len(matrix),k)): arr.extend(matrix[i])
        arr.sort()
        return arr[k-1]