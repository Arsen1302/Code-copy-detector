class Solution:
    def solution_548_2(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        col = [0] * n                                              # a list to count 1 in each column
        for i in range(m):
            for j in range(n-1, -1, -1):                           # start from the right, so we can use A[i][0] as a reference
                A[i][j] = (1-A[i][j]) if not A[i][0] else A[i][j]  # flip row if start of this row is 0
                col[j] += A[i][j]
        for j in range(1, n):                                      # flip column when necessary
            if (m % 2 and col[j] <= m // 2) or (not m % 2 and col[j] < m // 2):
                for i in range(m): A[i][j] = 1-A[i][j]
        return sum(sum(2**(n-1-j) * A[i][j] for j in range(n)) for i in range(m)) # calculate the sum