class Solution:
    """
    Time:   O(log(n))
    Memory: O(1)
    """

    def solution_888_2(self, num: int) -> int:
        steps = 0

        while num != 0:
            steps += 1
            if num &amp; 1:
                num -= 1
            else:
                num >>= 1

        return steps