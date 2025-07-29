class Solution:
    def solution_1470_1_1(self, q: List[List[int]]) -> int:
        @cache
        def solution_1470_1_2(i: int) -> int:
            return 0 if i >= len(q) else max(solution_1470_1_2(i + 1), q[i][0] + solution_1470_1_2(i + 1 + q[i][1]))
        return solution_1470_1_2(0)