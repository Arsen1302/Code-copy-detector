class Solution:
    def solution_1289_2(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = [0]*(right-left+1)
        for st, ed in ranges: 
            for x in range(st, ed+1): 
                if left <= x <= right: covered[x - left] = 1
        return all(covered)