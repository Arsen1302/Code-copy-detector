class Solution:
    def solution_136_1(self, A):
        n = len(A)
        l, r = 0, n - 1
        while l < r:
            m = (l + r + 1) // 2
            if A[m] > n - m: r = m - 1
            else: l = m
        return n - l - (A[l] < n - l)