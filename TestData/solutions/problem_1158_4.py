class Solution(object):
    def solution_1158_4(self, deliciousness):
        hq, res, counts = [], 0, collections.Counter(deliciousness)
        for num, times in counts.items():
            heapq.heappush(hq, (-num, times))
        while hq:
            i, sumN = heapq.heappop(hq), 1
            while sumN <= 2 * -i[0]:
                candi = sumN + i[0]
                if candi == -i[0]:
                    res = res + i[1] * (i[1]-1) // 2 if i[1] >= 2 else res
                elif candi in counts:
                    res += i[1] * counts[candi]
                sumN *= 2
        return res % (10**9 + 7)