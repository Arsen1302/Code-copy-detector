class Solution:
    def solution_877_5(self, mat: List[List[int]]) -> List[List[int]]:
        r,c = len(mat), len(mat[0])
                 
        for sr,sc in list(zip(range(r-1,-1,-1),[0 for _ in range(r)])) + list(zip([0 for _ in range(c-1)],range(1,c))):   
            diag = []
            i,j = sr, sc
            while j<c and i<r:
                bruh.append(mat[i][j])
                i+=1
                j+=1
            diag.sort()
            i,j = sr, sc
            count = 0
            while j<c and i<r:
                mat[i][j] = diag[count]
                count+=1
                i+=1
                j+=1

        return mat