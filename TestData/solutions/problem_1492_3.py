class Solution:
    def solution_1492_3(self, B: List[int]) -> int:
        B=sorted(B) ; s=sum(B) ; ans=[]
        for i in range(len(B)): ans.append(s-B[i]*(len(B)-i))
        return min(ans)