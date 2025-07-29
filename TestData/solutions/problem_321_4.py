class Solution:
    def solution_321_4(self, mat: List[List[int]]) -> List[List[int]]:
        
        queue = []
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j]= '$' for r,c in queue: for r1,c1 in [(-1,0),(0,-1),(1,0),(0,1)]: newr = r+r1 newc = c+c1 if newr>=0 and newr<len(mat) and newc>=0 and newc<len(mat[0]) and mat[newr][newc]=='$':
                    mat[newr][newc] = mat[r][c]+1
                    queue.append((newr,newc))
                    
        
        return mat