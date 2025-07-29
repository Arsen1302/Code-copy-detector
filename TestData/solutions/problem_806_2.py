class Solution:
    def solution_806_2(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        x, y = king
        queens = {(x, y) for x, y in queens}
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for k in range(1, 8):
                    xx, yy = x+k*dx, y+k*dy
                    if (xx, yy) in queens: 
                        ans.append([xx, yy])
                        break 
        return ans