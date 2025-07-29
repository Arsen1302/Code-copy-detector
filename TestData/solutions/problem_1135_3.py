class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(1)
    """

    MOD = 10 ** 9 + 7

    def solution_1135_3(self, n: int) -> int:
        return reduce(lambda x, y: ((x << y.bit_length()) | y) % self.MOD, range(1, n + 1))