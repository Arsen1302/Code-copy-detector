class Solution:
    def solution_523_5(self, A: List[List[int]], B: List[List[int]]) -> int:
        N = len(A)
        Aones = [(x, y) for x in range(N) for y in range(N) if A[x][y]]
        Bones = [(x, y) for x in range(N) for y in range(N) if B[x][y]]
        transformationCount = defaultdict(int)
        
        for Ax, Ay in Aones:
            for Bx, By in Bones:
                vector = (Bx - Ax, By - Ay)
                transformationCount[vector] += 1
                
        return max(transformationCount.values(), default = 0)