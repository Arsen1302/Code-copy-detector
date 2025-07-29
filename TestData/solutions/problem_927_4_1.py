class Solution:
    def solution_927_4_1(self, grid: List[List[int]]) -> bool:
        d = { # direction
            'E': (0,1), 'W': (0,-1), 'N': (-1,0), 'S': (1,0),
        }
        valid_path = {
            1: {'E': [1, 3, 5], 'W': [1, 4, 6]},
            2: {'N': [2, 3, 4], 'S': [2, 5, 6]},
            3: {'W': [1, 4, 6], 'S': [2, 5, 6]},
            4: {'E': [1, 3, 5], 'S': [2, 5, 6]},
            5: {'N': [2, 3, 4], 'W': [1, 4, 6]},
            6: {'N': [2, 3, 4], 'E': [1, 3, 5]},
        }
        
        def solution_927_4_2(i, j):
            if (i,j) == (m-1,n-1):
                return True
            visited.add((i,j)) 
            for dr, valid_types in valid_path[grid[i][j]].items():
                i_nxt, j_nxt = i + d[dr][0], j + d[dr][1]
                if (i_nxt, j_nxt) not in visited and\
                    0 <= i_nxt < m and 0 <= j_nxt < n:
                    if grid[i_nxt][j_nxt] in valid_types:
                        if solution_927_4_2(i_nxt, j_nxt):
                            return True
            return False
        
        m, n = len(grid), len(grid[0])
        visited = set()
        return solution_927_4_2(0, 0)