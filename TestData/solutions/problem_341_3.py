class Solution:
    def solution_341_3(self, candyType: List[int]) -> int:
        n=len(candyType)
        l=set(candyType)
        if len(l)==n//2:
            return len(l)
        elif len(l)>n//2:
            return n//2
        else:
            return len(l)