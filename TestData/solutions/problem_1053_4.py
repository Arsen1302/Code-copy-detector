class Solution:
    def solution_1053_4(self, n: int, R: List[int]) -> List[int]:
        if R[0]<=R[-1]: return range(R[0],R[-1]+1)
        return sorted(set(range(1,n+1)) - set(range(R[-1]+1,R[0])))