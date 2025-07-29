class Solution:
    def solution_1361_4_1(self, land: List[List[int]]) -> List[List[int]]:
        
        movements = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        def solution_1361_4_2(i, j):
            nonlocal r2, c2
            land[i][j] = 2 # visited
            for row, col in movements:
                r = i + row
                c = j + col
                
                if 0 <= r < len(land) and 0 <= c < len(land[0]) and land[r][c] == 1:
                    r2 = max(r2, r)
                    c2 = max(c2, c)
                    solution_1361_4_2(r, c)
            
        answer = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:
                    r2, c2 = i, j
                    solution_1361_4_2(i, j)
                    answer.append((i, j, r2, c2))
        
        return answer