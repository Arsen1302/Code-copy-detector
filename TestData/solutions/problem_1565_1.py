class Solution:
    """
    Time:   O(log10(n)*k)
    Memory: O(log10(n))
    """

    def solution_1565_1(self, num: int, k: int) -> int:
        str_num = str(num)
        return sum(
            num % int(str_num[i - k:i]) == 0
            for i in range(k, len(str_num) + 1)
            if int(str_num[i - k:i]) != 0
        )