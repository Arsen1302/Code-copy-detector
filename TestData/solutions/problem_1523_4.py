class Solution:
    def solution_1523_4(self, directions: str) -> int:
        has_stationary, right, collisions = False, 0, 0
        for direction in directions:
            if direction == 'R':
                right += 1
            elif (direction == 'L' and (has_stationary or right > 0)) or direction == 'S':
                collisions += (1 if direction == 'L' else 0) + right
                right = 0
                has_stationary = True
        return collisions