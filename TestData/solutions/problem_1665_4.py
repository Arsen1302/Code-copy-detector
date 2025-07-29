class Solution:
    def solution_1665_4(self, A):
        A = list(map(sorted, zip(*A)))
        ans, j = 1, 0
        for i in range(1, len(A[0])):
            if A[0][i] > A[1][j]: j += 1
            else: ans += 1
        return ans