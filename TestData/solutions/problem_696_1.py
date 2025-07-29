class Solution:
    def solution_696_1(self, S: str, N: int) -> bool:
        for x in range(N, 0, -1):
            if bin(x)[2:] not in S: return False 
        return True