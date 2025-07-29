class Solution:
    def solution_1595_4(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        unit = num % 10
        for i in range(1, 11):
            if (i * k) % 10 == unit:
                if i * k <= num:
                    return i
                else:
                    break
        return -1