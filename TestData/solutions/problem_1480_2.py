class Solution:
    def solution_1480_2(self, n: List[int], o: int) -> int:
        n = sorted(n)
        for i in range(len(n)) :
            if o == n[i]:
                o *= 2
        return o