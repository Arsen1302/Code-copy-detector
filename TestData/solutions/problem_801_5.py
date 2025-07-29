class Solution:
    def solution_801_5(self, position: List[int]) -> int:
        pos_at_zero = sum(pos % 2 == 0 for pos in position)
        return min(pos_at_zero, len(position) - pos_at_zero)