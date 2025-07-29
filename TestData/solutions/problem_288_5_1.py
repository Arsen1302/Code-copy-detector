class Solution:
    def solution_288_5_1(self, mat: List[List[int]]) -> List[int]:
       flip=0
        res=[]
        R=len(mat)
        C=len(mat[0])
        def solution_288_5_2(r,c):
            if r<0 or c<0 or r>=R or c>=C:
                return False
            return True
        def solution_288_5_3(r,c):
            temp=[]
            while solution_288_5_2(r,c):
                temp.append(mat[r][c])
                r-=1
                c+=1
            if flip:
                temp.reverse()
            res.extend(temp)
        for i in range(R):
            solution_288_5_3(i,0)
            flip=not flip
        for i in range(1,C):
            solution_288_5_3(R-1,i)
            flip=not flip
        
        return res