class Solution:
    def solution_1092_3_1(self, A, B):
        n = len(A)
        def solution_1092_3_2(A, B):
            l =  n // 2 - 1
            while l >= 0 and A[l] == A[n - l - 1]:
                l -= 1
            if A[:l+1] == B[:-l-2:-1] or A[:-l-2:-1] == B[:l+1]: return True
        return solution_1092_3_2(A, B) or solution_1092_3_2(B, A)