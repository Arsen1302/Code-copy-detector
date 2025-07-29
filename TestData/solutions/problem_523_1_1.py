class Solution:
    def solution_523_1_1(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        bestOverlap = 0

        def solution_523_1_2(dr, dc):
            overlap = 0
            for r in range(n):
                for c in range(n):
                    nr, nc = r + dr, c + dc
                    if nr in range(n) and nc in range(n) and img1[nr][nc] == 1 and img2[r][c] == 1:
                        overlap += 1

            return overlap

        for r in range(-n, n):
            for c in range(-n, n):
                bestOverlap = max(solution_523_1_2(r, c), bestOverlap)

        return bestOverlap