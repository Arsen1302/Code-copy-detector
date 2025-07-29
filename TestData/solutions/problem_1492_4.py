class Solution:
    def solution_1492_4(self, B: List[int]) -> int:
        B=sorted(B) ; S=sum(B) ; ans=S
        for i in range(len(B)):
            currS=S-B[i]*(len(B)-i)
            if currS<ans: ans=currS
        return ans