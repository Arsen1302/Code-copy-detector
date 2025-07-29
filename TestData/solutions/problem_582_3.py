class Solution:
    def solution_582_3(self, A: List[int]) -> bool:
        if sorted(A)==A or sorted(A,reverse=True)==A:
            return True
        return False