class Solution:
    def solution_1321_4(self, rungs: List[int], dist: int) -> int:
        count = 0
        if rungs[0] > dist:
            m = rungs[0]
            m = (m - 1) // dist
            count += m
        for i in range (len(rungs) - 1):
            k = rungs[i+1] - rungs[i]
            if k > dist:
                
                n = (k-1) // dist
                count += n
        return count