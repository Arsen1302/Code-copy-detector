class Solution:
    def solution_374_4(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        prev_index = len(pairs) - 1
        result = 1
        for i in range(len(pairs) - 2, -1, -1):
            if pairs[i][1] < pairs[prev_index][0]:
                prev_index = i
                result += 1
        return result
        
        pairs.sort()
        dp = [1] * len(pairs)
        for i in range(len(pairs) - 1, -1, -1):
            for j in range(i + 1, len(pairs)):
                if pairs[i][1] < pairs[j][0]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)