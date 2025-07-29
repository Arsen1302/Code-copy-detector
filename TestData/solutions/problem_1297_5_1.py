class Solution:
    def solution_1297_5_1(self, mat: List[List[int]]) -> List[int]:
        self.r=0
        self.c=0
        rows=len(mat)
        col=len(mat[0])
        def solution_1297_5_2(l,r):
            if l>=r:
                return False
            mid=l+r>>1
            for x in range(rows):
                top=mat[x-1][mid] if x-1>=0 else -1
                bot=mat[x+1][mid] if x+1<rows else -1
                right=mat[x][mid+1] if mid+1<col else -1
                left=mat[x][mid-1] if mid-1>=0 else -1
                if mat[x][mid]>top and mat[x][mid]>left and mat[x][mid]>right and mat[x][mid]>bot:
                    self.r=x
                    self.c=mid
                    return True
            if solution_1297_5_2(mid+1, r):
                return True
            if solution_1297_5_2(l, mid-1):
                return True
            return False
        solution_1297_5_2(0,col)
        return [self.r, self.c]