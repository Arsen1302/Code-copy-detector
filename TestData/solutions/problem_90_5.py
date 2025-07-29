class Solution:
    def solution_90_5(self, left: int, right: int) -> int:
        while right > left:
            right = right &amp; (right - 1)
        return right