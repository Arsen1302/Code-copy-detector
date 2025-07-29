class Solution:
    """
    Time:   O(log(n))
    Memory: O(log(n))
    """

    def solution_888_1(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + self.solution_888_1(num - 1 if num &amp; 1 else num >> 1)