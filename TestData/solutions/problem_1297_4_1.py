class Solution:
    def solution_1297_4_1(self):
        self.mat = 0
    def solution_1297_4_2(self, mat: List[List[int]]) -> List[int]:
        self.mat = mat
        m = len(mat)
        n = len(mat[0])
        i, j = 0, 0
        while i < m:
            while j < n:
                if (self.solution_1297_4_3(i, j-1)<self.solution_1297_4_3(i, j)
                    and self.solution_1297_4_3(i, j)>self.solution_1297_4_3(i, j+1)
                    and self.solution_1297_4_3(i, j)>self.solution_1297_4_3(i-1, j)
                    and self.solution_1297_4_3(i, j)>self.solution_1297_4_3(i+1, j)):
                    return [i, j]
                # left
                elif self.solution_1297_4_3(i, j) < self.solution_1297_4_3(i, j-1):
                    j = j-1
                # right
                elif self.solution_1297_4_3(i, j) < self.solution_1297_4_3(i, j+1):
                    j = j+1
                # top
                elif self.solution_1297_4_3(i, j) < self.solution_1297_4_3(i-1, j):
                    i = i-1
                # bottom
                elif self.solution_1297_4_3(i, j) < self.solution_1297_4_3(i+1, j):
                    i = i + 1
                
                
                
    def solution_1297_4_3(self, i, j) -> int:
        m, n = len(self.mat), len(self.mat[0])
        if i<0 or j<0 or i>=m or j>=n:
            return -1
        else:
            return self.mat[i][j]