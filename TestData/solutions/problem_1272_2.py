class Solution:
    def solution_1272_2(self, s: str) -> bool:
        count0 = count1 = max0 = max1 = 0
        for c in s:
            if c == '0':
                count1 = 0
                count0 += 1
                max0 = max(max0, count0)
            else:
                count0 = 0
                count1 += 1
                max1 = max(max1, count1)
        return (max1 > max0)