class Solution:
    def solution_670_5_1(self, eq):
        return ord(eq[0]) - ord('a'), eq[1:3], ord(eq[3]) - ord('a')
    
    def solution_670_5_2(self, equations: List[str]) -> bool:
        graph = [[0] * 26 for _ in range(26)]
        for eq in equations:
            x, r, y = self.solution_670_5_1(eq)
            if r == '==':
                graph[x][y], graph[y][x] = 1, 1
            elif x == y:
                return False
            
        for k in range(26):
            for i in range(26):
                if graph[i][k]:
                    for j in range(26):
                        if graph[k][j]:
                            graph[i][j] = 1
                            
        for eq in equations:
            x, r, y = self.solution_670_5_1(eq)
            if r == '!=' and graph[x][y]:
                return False
        return True