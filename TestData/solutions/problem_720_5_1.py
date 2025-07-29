class Solution:
    def solution_720_5_1(self, instructions: str) -> bool:
        def solution_720_5_2(i, j, dir):
            for char in instructions:
                if char == 'G':
                    if dir == 0:
                        i -= 1
                    elif dir == 1:
                        j -= 1
                    elif dir == 2:
                        i += 1
                    else:
                        j += 1
                elif char == 'L':
                    dir = (dir + 1) % 4
                else:
                    dir = (dir - 1) % 4
            return i, j, dir
        
        i, j, dir = 0, 0, 0
        for _ in range(4):
            i, j, dir = solution_720_5_2(i, j, dir)
            if i == 0 and j == 0:
                return True
        return False