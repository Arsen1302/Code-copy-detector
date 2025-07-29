class Solution:
    def solution_1440_5(self, rings: str) -> int:
        counts = [[False for i in range(3)] for j in range(10)]
        for i in range(0, len(rings), 2):
            if rings[i] == 'B':
                counts[int(rings[i+1])][0] = True
            elif rings[i] == 'R':
                counts[int(rings[i+1])][1] = True
            elif rings[i] == 'G':
                counts[int(rings[i+1])][2] = True
        return sum([1 for c in counts if sum(c) == 3])