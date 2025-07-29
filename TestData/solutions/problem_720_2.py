class Solution:
    def solution_720_2(self, instructions: str) -> bool:
        direc, pos = 0, [0, 0]
        for c in instructions:
            if c == "L": direc = (direc + 1) % 4
            elif c == "R": direc = (direc - 1) % 4
            elif c == "G":
                if direc == 0: pos[1] += 1
                elif direc == 1: pos[0] -= 1
                elif direc == 2: pos[1] -= 1
                else: pos[0] += 1
        return pos == [0, 0] or direc != 0