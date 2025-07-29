class Solution:
    def solution_613_4(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(1, n):   # for each row (skipping the first),
            for j in range(n):  # process each element in the row
                matrix[i][j] += min(matrix[i-1][j],          # the minimum sum of the element directly above the current one
                                    matrix[i-1][j-(j>0)],    # the minimum sum of the element above and to the left of the current one
                                    matrix[i-1][j+(j<n-1)])  # the minimum sum of the element above and to the right of the current one
        return min(matrix[-1])  # get the minimum sum from the last row