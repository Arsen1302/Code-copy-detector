class Solution:
    def solution_767_1_1(self, piles: List[int]) -> int:
        suffix_sum = self._suffix_sum(piles)

        @lru_cache(None)
        def solution_767_1_2(pile: int, M: int, turn: bool) -> Tuple[int, int]:
            # turn: true - alex, false - lee
            sum_alex, sum_lee = suffix_sum[pile], suffix_sum[pile]

            for next_pile in range(pile + 1, min(pile + 2 * M + 1, len(piles) + 1)):
                sum_alex_next, sum_lee_next = solution_767_1_2(
                    next_pile, max(M, next_pile - pile), not turn
                )
                range_sum = suffix_sum[pile] - suffix_sum[next_pile]

                if turn:
                    if sum_lee_next < sum_lee:
                        sum_alex = sum_alex_next + range_sum
                        sum_lee = sum_lee_next
                else:
                    if sum_alex_next < sum_alex:
                        sum_alex = sum_alex_next
                        sum_lee = sum_lee_next + range_sum

            return sum_alex, sum_lee

        return solution_767_1_2(0, 1, True)[0]