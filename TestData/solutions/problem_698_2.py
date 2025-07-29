class Solution:
    def solution_698_2(self, A: List[int]) -> List[bool]:
        s='';l=[]
        for i in A:
            s+=str(i)
            l.append(int(s,2)%5==0)
        return l