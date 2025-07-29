class Solution:
    def solution_561_4(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # direction: 0-north, 1-east, 2, south, 3-west
        direction = x = y = 0
        max_distance = 0
        obstacles = set((x, y) for x, y in obstacles)
        for command in commands:
            if command == -2:
                direction = (direction - 1) % 4
                continue
            elif command == -1:
                direction = (direction + 1) % 4
                continue
            elif 0 < command < 10:
                if direction == 0:
                    for _ in range(command):
                        if (x, y + 1) in obstacles:
                            break
                        else:
                            y += 1
                elif direction == 1:
                    for _ in range(command):
                        if (x + 1, y) in obstacles:
                            break
                        else:
                            x += 1
                elif direction == 2:
                    for _ in range(command):
                        if (x, y - 1) in obstacles:
                            break
                        else:
                            y -= 1
                elif direction == 3:
                    for _ in range(command):
                        if (x - 1, y) in obstacles:
                            break
                        else:
                            x -= 1
                max_distance = max(max_distance, x * x + y * y)
        return max_distance