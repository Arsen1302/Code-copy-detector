class Solution:
    """
    Time:   O(log10(n))
    Memory: O(1)
    """

    def solution_1565_2(self, num: int, k: int) -> int:
        power = 10 ** (k - 1)
        tmp, window = divmod(num, 10 * power)

        count = int(window and not num % window)
        while tmp:
            tmp, digit = divmod(tmp, 10)
            window = digit * power + window // 10
            count += window and not num % window

        return count