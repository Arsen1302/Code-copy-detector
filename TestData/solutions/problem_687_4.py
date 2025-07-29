class Solution:
    def solution_687_4(self, tops: List[int], bottoms: List[int]) -> int:
        nlen = len(tops)
        top_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        bottom_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        both_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        i = 0
        while i < nlen:
            top_count[tops[i]] += 1
            bottom_count[bottoms[i]] += 1
            if tops[i] == bottoms[i]:
                both_count[bottoms[i]] += 1
            i += 1
        
        print(top_count)
        print(bottom_count)
        print(both_count)
        res = 30000
        for i in range(1, 7):
            if top_count[i] + bottom_count[i] - both_count[i] == nlen:
                res = min(res, min(top_count[i], bottom_count[i]) - both_count[i])
        if res == 30000:
            return -1
        return res