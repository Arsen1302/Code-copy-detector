class Solution:
    def solution_1010_1(self, n: int, left: List[int], right: List[int]) -> int:
        if left and not right:
            return max(left)
        if not left and right:
            return n - min(right)
        if not left and not right:
            return 0
        if left and right:
            return max(max(left), n - min(right))