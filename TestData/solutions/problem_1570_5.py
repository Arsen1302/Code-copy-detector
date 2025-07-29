class Solution:
    def solution_1570_5(self, bottom: int, top: int, special: List[int]) -> int:
        c=0
        l=[]
        special.sort()
        a=special[0]-bottom
        b=top-special[-1]
        for i in range(len(special)-1):
            l.append(special[i+1]-special[i]-1)
        if len(l)>=1:
            c=max(l)
        return max(a,b,c)