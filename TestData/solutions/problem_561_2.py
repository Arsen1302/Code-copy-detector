class Solution:
    def solution_561_2(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        facing = best = 0
        distance = lambda x, y: x**2 + y**2
        current = (0, 0)
        obstacles = {(p[0], p[1]) for p in obstacles}

        for c in commands:
            if c == -1:
                facing = (facing + 1) % 4
            elif c == -2:
                facing = (facing + 3) % 4
            elif 1 <= c <= 9:
                for i in range(c):
                    newx = current[0] + directions[facing][0]
                    newy = current[1] + directions[facing][1]
                    if (newx, newy) not in obstacles:
                        current = (newx, newy)
                        best = max(best, distance(current[0], current[1]))
                    else:
                        break
            else:
                raise ValueError
        return best