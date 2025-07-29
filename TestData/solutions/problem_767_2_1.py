class Solution:
    def solution_767_2_1(self, piles: List[int]) -> int:
        suffix_sum = self._suffix_sum(piles)

        @lru_cache(None)
        def solution_767_2_2(pile: int, M: int) -> int:
            sum_next_player = suffix_sum[pile]

            for next_pile in range(pile + 1, min(pile + 2 * M + 1, len(piles) + 1)):
                sum_next_player = min(
                    sum_next_player, solution_767_2_2(next_pile, max(M, next_pile - pile))
                )

            sum_player = suffix_sum[pile] - sum_next_player

            return sum_player

        return solution_767_2_2(0, 1)