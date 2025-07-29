class Solution:
    def solution_1675_3(self, n: List[str], h: List[int]) -> List[str]:
        return [c for _, c in sorted(zip(h, n), reverse=True)]