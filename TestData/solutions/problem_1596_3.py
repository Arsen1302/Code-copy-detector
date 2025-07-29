class Solution:
    def solution_1596_3(self, s: str, k: int) -> int:
        n = len(s)
        total0 = 0
        for char in s:
            if char == '0':
                total0 += 1
        if total0 == n:
            return n
        curr, temp, total1 = 0, 1, 0
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                curr += temp
                if curr > k:
                    return total0 + total1
                total1 += 1
            temp *= 2
        return n