class Solution:
    def solution_1010_5(self, n: int, left: List[int], right: List[int]) -> int:
        left_max = max(left) if left else 0
        right_max = n - min(right) if right else 0
        return max(left_max, right_max)