class Solution:
    def solution_1423_2(self, plants: List[int], capacity: int) -> int:
        s, p, c = 0, -1, capacity
        for i, e in enumerate(plants):
            if e <= c: s += i - p; c -= e
            else: s += p + i + 2; c = capacity - e
            p = i
        return s