class Solution:
    def solution_222_3(self, A: List[int]) -> int:
        l = 0
        res = 0
        for r, num in enumerate(A):
            if r - l < 2:
                continue
            if num - A[r-1] == A[l+1] - A[l]:
                res += r - l - 1
            else:
                l = r - 1
        return res