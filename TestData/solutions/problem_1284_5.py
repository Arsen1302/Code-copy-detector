class Solution:
    def solution_1284_5(self, n: int) -> int:
        # 100 -> 99 97 94 90 85 79 72 64 55 45 34 22 9 0
        # 14 -> 13 11 8 4 0
        # 6 -> 5 3 0
        remain = n
        cur = 1

        ret = 0
        while remain > 0:
            remain -= cur
            ret += 1
            cur += 1
        
        return ret