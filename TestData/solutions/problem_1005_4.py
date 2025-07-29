class Solution:
    def solution_1005_4(self, path: str) -> bool:
        coor = [0, 0]
        coors = [[0, 0]]
        for i in path:
            if i == 'N': coor[1] += 1
            elif i == 'E': coor[0] += 1
            elif i == 'S': coor[1] -= 1
            else: coor[0] -= 1
            if coor in coors: return True
            coors.append(coor[:])
        return False