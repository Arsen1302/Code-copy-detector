class Solution:
    def solution_1536_4(self, num: int) -> int:
        lst = [int(i) for i in str(num)]
        p = [[], []]
        for i, v in enumerate(lst):
            j = v &amp; 1
            p[j].append(v)
            lst[i] = j
        for i in p:
            i.sort()
        ret = 0
        for j in lst:
            ret = ret * 10 + p[j].pop()
        return ret