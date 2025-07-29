class Solution:
    def solution_288_4(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)-1  # index upperbound
        columns = len(mat[0])-1  # index upperbound
        up = False # Next iteration flag
        ans = [mat[0][0]]
        lastPoint = [0,0]
        
        while True:
            r,c = lastPoint
            
            # upward initialisation (row--, cols++)
            if up:
                if r<rows:
                    r+=1
                else:# No more rows. (r>= rows)
                    r = r  
                    c+=1
                    if c>columns:  
                        # No more columns too.
                        return ans
                    
                # print('upstart',r,c)
                # boundary conditions to end upward traverse
                while c<=columns and r>=0:  # right_border, upper_border
                    print(r,c)
                    ans.append(mat[r][c])
                    lastPoint = [r,c]
                    r-=1
                    c+=1
                
                up = False
            
            # downward initailisation
            # row++ cols--
            else: 
                if c<columns:
                    c+=1
                else: # No more Columns. (c>=columns)
                    c = c  
                    r+=1
                    if r>rows: 
                        # No more Rows too.
                        return ans
                    
                # print('godown',r,c)
                # boundary condition to end downward traverse
                while r<=rows and c>=0:  # down_border and left_border 
                    print(r,c)
                    ans.append(mat[r][c])
                    lastPoint = [r,c]
                    r+=1
                    c-=1
                
                up = True
        
        # print(ans)
        return ans