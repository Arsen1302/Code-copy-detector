class Solution:
    def solution_524_5(self, rec1: List[int], rec2: List[int]) -> bool:
        # a,b,c,d = 0,1,2,3
        a1 = (min(rec1[2],rec2[2]) - max(rec1[0],rec2[0]))
        a2 = (min(rec1[3],rec2[3]) - max(rec1[1],rec2[1]))
        if a1 > 0 and a2 > 0:
            return True
        return False