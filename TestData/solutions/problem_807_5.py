class Solution:
    def solution_807_5(self, n: int, R: List[int]) -> int:
        DP, S, m = [[1]+[0]*(i-1) for i in R], [0]*6, 10**9 + 7
        for _ in range(1,n):
            for j in range(6): S[j], _ = sum(DP[j]), DP[j].pop()
            for j in range(6): DP[j] = [sum(S) - S[j]] + DP[j]
        return sum(sum(DP,[])) % m