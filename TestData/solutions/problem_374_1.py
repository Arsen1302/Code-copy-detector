class Solution:
    def solution_374_1(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        rt = 1
        l = pairs[0]
        for r in range(1,len(pairs)):
            if l[1] < pairs[r][0]:
                rt += 1 
                l = pairs[r]
            elif pairs[r][1]<l[1]:
                l = pairs[r]
        return rt