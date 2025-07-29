class Solution:
    def solution_1054_5(self, piles: List[int]) -> int:
        piles.sort()
        return sum(piles[-len(piles)*2//3::2])