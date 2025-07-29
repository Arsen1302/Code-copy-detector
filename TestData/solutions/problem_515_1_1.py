class Solution:
    def solution_515_1_1(self, grid: List[List[int]]) -> int:
        N = len(grid)
        DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        
		address = {}
        def solution_515_1_2(row, column, island_id):
            queue = deque([(row, column, island_id)])
            visited.add((row, column))
            area = 1
            while queue: 
                row, column, island_id = queue.pop()
                address[(row, column)] = island_id
                for direction in DIRECTIONS:
                    r, c = row + direction[0], column + direction[1]
                    if r in range(N) and c in range(N) and grid[r][c] == 1 and (r, c) not in visited:
                        queue.append((r, c, island_id))
                        visited.add((r, c))
                        area += 1
            return area
        
        visited = set()
        area = {}
        island_id = 0
        for row in range(N):
            for column in range(N):
                if grid[row][column] == 1 and (row, column) not in visited:
                    area[island_id] = solution_515_1_2(row, column, island_id)
                    island_id += 1
                    
        if len(address.keys()) == N**2: return N**2   
        
        largest_area = 1
        for row in range(N):
            for column in range(N):
                if grid[row][column] == 1: continue
                neighbours = set()
                large_area = 1
                for direction in DIRECTIONS:
                    r, c = row + direction[0], column + direction[1]
                    if r in range(N) and c in range(N) and grid[r][c] == 1 and address[(r, c)] not in neighbours:
                        neighbours.add(address[(r, c)])
                        large_area += area[address[(r, c)]]
                largest_area = max(largest_area, large_area)
                
        return largest_area