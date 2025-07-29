class Solution:
    def solution_1054_4(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        k = len(piles)//3
        i = len(piles)-1
        j = 0
        while i>0 and j<k:
            res += piles[i-1]
            i-=2
            j+=1
        return res