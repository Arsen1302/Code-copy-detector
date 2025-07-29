class Solution:
    def solution_823_5(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
    
       # if upper+lower is not equal to the sum of colsum, return []
        if (upper+lower)!=sum(colsum):
            return []
		# if colsum[j]==2, then both the upper and lower elements need to be 1. However, if the number of 2 in colsum is more than upper or lower, then return []
        if colsum.count(2)>upper or colsum.count(2)>lower:
            return []
    
        m, n = 2, len(colsum)    
        A = [[0]*n for i in range(m)]
    
        # for colsum[n]==2, necessarilly to assign 1 and 1 to both upper and lower elements.
        for j in range(n):
            if colsum[j]==2:
                A[0][j], A[1][j] = 1, 1
                upper -= 1
                lower -= 1
                colsum[j] = 0

       # the greedy part
        for i in range(m):
            for j in range(n):
                if colsum[j]>0:
                    if i==0 and upper>0:
                        A[i][j] = 1
                        upper -= 1
                        colsum[j] -= 1
                    elif i==1 and lower>0:
                        A[i][j] = 1
                        lower -= 1
                        colsum[j] -= 1
        return A