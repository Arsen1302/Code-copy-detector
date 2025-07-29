class Solution:
    def solution_328_1(self, wall: List[List[int]]) -> int:
        count = defaultdict(int)
        tot = len(wall)
        if tot == 1 and len(wall[0]) > 1:
            return 0
        elif tot == 1 and len(wall[0]) == 1:
            return 1
        
        for w in wall:
            s = 0 
            for i in range(len(w)):
                s += w[i]
                count[s] += 1
            count[s] -= 1

        return tot - max(count.values())