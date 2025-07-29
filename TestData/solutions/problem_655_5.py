class Solution:
    def solution_655_5(self, A, K):
        csum, ans = 0, 0
        D = [0] * K
        D[0] = 1
        for i in A:
            csum = (csum + i) % K
            ans += D[csum]
            D[csum] += 1
        return ans