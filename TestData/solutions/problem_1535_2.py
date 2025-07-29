class Solution:
    def solution_1535_2(self, C: List[int], k: int) -> int:
        lo=0 ; hi=sum(C)//k
        while lo<hi:
            mid=(lo+hi)//2+1
            if sum(c//mid for c in C)>=k: lo=mid
            else: hi=mid-1
        return lo