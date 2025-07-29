class Solution:
    def solution_1297_3(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            for j in range(m):
                if i-1 < 0: # checking up
                    up = -1
                else:
                    up = mat[i-1][j]
                if i+1 >= n: # checking down
                    down = -1
                else:
                    down = mat[i+1][j]
                if j-1 < 0: # checking left
                    left = -1
                else:
                    left = mat[i][j-1]
                if j+1 >= m: # checking right
                    right = -1
                else:
                    right = mat[i][j+1]
                if mat[i][j] > max(up, left, right, down):
                    return [i,j]
        return False