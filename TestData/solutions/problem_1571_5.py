class Solution:
    def solution_1571_5(self, A: List[int]) -> int:
        n = len(A)
        ans= 0
        for i in range(32):
            maxCol = 0
            for j in range(n):
                if (A[j]>>i) &amp; 1 == 1:
                    maxCol += 1
            ans = max(ans,maxCol)
        return ans