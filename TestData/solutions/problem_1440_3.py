class Solution:
    def solution_1440_3(self, rings: str) -> int:
        r = []
        g = []
        b = []
        ring_nums = set()
        count = 0
        for i in range(0, len(rings)):
            if rings[i] == 'R':
                r.append(int(rings[i+1]))
                if rings[i+1] not in ring_nums:
                    ring_nums.add(int(rings[i+1]))
            elif rings[i] == 'G':
                g.append(int(rings[i+1]))
                if rings[i+1] not in ring_nums:
                    ring_nums.add(int(rings[i+1]))
            elif rings[i] == 'B':
                b.append(int(rings[i+1]))
                if rings[i+1] not in ring_nums:
                    ring_nums.add(int(rings[i+1]))
        for i in ring_nums:
            if i in r and i in g and i in b:
                count += 1
        return count