class Solution:
    def solution_1657_4(self, matrix: List[List[int]], numSelect: int) -> int:
        ans = 0
        m_ones = [{i for i, v in enumerate(row) if v} for row in matrix]
        for comb in combinations(range(len(matrix[0])), numSelect):
            set_comb = set(comb)
            ans = max(ans, sum(s.issubset(set_comb) for s in m_ones))
        return ans