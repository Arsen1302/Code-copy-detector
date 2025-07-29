class Solution:
    def solution_1289_5(self, ranges: List[List[int]], left: int, right: int) -> bool:
        merge = []
        for start, end in sorted(ranges): 
            if merge and start <= merge[-1][1]+1: 
                merge[-1][1] = max(merge[-1][1], end)
            else: merge.append([start, end])
        return any(x <= left <= right <= y for x, y in merge)