class Solution:
    def solution_524_3(self, R1: List[int], R2: List[int]) -> bool:
        return not (R1[0]>=R2[2] or R1[1]>=R2[3] or R1[2]<=R2[0] or R1[3]<=R2[1])