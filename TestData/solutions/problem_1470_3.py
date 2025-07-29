class Solution:
    def solution_1470_3(self, questions: List[List[int]]) -> int:
        dp = [(0, 0)] * (len(questions) + 1)
        for i in range(len(questions) - 1, -1, -1):
            score, delay = questions[i]
            dp[i] = score + (max(dp[i + delay + 1]) if i + delay + 1 < len(questions) else 0), max(dp[i + 1])
        return max(dp[0])