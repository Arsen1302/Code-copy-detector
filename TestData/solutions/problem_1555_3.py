class Solution:
    def solution_1555_3(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guarded = set()
        guard_set = set()
        wall_set = set()
        
		for guard in guards:  guard_set.add((guard[0], guard[1]))
        for wall in walls: wall_set.add((wall[0], wall[1]))
		
		# left, right, bottom, top
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
		
        # find all guarded
        for guard in guards:
            for dx, dy in directions:
                x, y = guard
                
				# travel one direction
                while 0 <= x + dx < m and 0 <= y + dy < n:
                    x, y = x + dx , y + dy
                    if (x, y) in guard_set or (x, y) in wall_set: break
                    guarded.add((x, y))
         
		# count unguarded
        not_guarded_count = 0
        for i in range(m):
            for j in range(n):
                if (i,j) not in guarded and (i, j) not in wall_set and (i, j) not in guard_set:
                    not_guarded_count += 1
        
        return not_guarded_count