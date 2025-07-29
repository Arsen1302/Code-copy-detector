class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    def solution_888_3(self, num: int) -> int:
        if num == 0:
            return 0
        return num.bit_length() - 1 + num.bit_count()