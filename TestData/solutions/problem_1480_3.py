class Solution:
    def solution_1480_3(self, n: List[int], o: int) -> int:
        while o in n:
            o *= 2
        return o