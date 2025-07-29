class Solution:
    def solution_914_5(self, flips: List[int]) -> int:

        l=len(flips)
        summ=0
        actual=0
        ans=0
        for i in range(l):
            summ+=flips[i]
            actual+=(i+1)
            if summ==actual:
                ans+=1
        return ans