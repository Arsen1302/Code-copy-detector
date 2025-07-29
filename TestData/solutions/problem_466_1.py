class Solution:
    def solution_466_1(self, A: List[int]) -> bool:
        for i, a in enumerate(A):
            if (abs(a - i) > 1):
                return False
        
        return True