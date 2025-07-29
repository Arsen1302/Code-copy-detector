class Solution:
    def solution_760_4(self, dominoes: List[List[int]]) -> int:
        
        d, c = dict(), 0
        for i in dominoes:
            if i[0] > i[1]:
                i[0], i[1] = i[1], i[0]

            if (i[0], i[1]) not in d:
                d[(i[0], i[1])] = 1
            else:
                d[(i[0], i[1])] += 1

        for j in d:
            if d[j] > 1:
                c += d[j] * (d[j] - 1) // 2
        return c