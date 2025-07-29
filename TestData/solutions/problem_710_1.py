class Solution:
    def solution_710_1(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        d = {}
        for i in range(R):
            for j in range(C):
                d[(i,j)] = d.get((i,j),0) + abs(r0-i) + abs(c0-j)
        return [list(i) for i,j in sorted(d.items(), key = lambda x : x[1])]