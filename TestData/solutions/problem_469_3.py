class Solution:
    def solution_469_3(self, N, K):
        ans = 0
        while K > 1:
            ans ^= ((K &amp; 1) ^ 1)
            K = (K >> 1) + (K &amp; 1)
        return ans