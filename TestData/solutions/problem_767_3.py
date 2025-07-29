class Solution:
    def solution_767_3(self, piles: List[int]) -> int:
        suffix_sum = self._suffix_sum(piles)

        dp = [[0] * (len(piles) + 1) for _ in range(len(piles) + 1)]

        for pile in reversed(range(len(piles))):
            for M in reversed(range(len(piles))):
                sum_next_player = suffix_sum[pile]

                for next_pile in range(pile + 1, min(pile + 2 * M + 1, len(piles) + 1)):
                    sum_next_player = min(
                        sum_next_player, dp[next_pile][max(M, next_pile - pile)]
                    )

                sum_player = suffix_sum[pile] - sum_next_player

                dp[pile][M] = sum_player

        return dp[0][1]