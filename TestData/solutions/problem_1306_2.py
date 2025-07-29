class Solution:
def solution_1306_2(self, mat: List[List[int]], k: int) -> List[List[int]]:
    
    top = 0
    bottom = len(mat)-1
    left = 0
    right = len(mat[0])-1
    res = []
	
    # storing in res all the boundry matrix elements.
    while left<right and top<bottom:
        local=[]
        for i in range(left,right+1):
            local.append(mat[top][i])
        top+=1
		
        for i in range(top,bottom+1):
            local.append(mat[i][right])
        right-=1
		
        for i in range(right,left-1,-1):
            local.append(mat[bottom][i])
        bottom-=1
		
        for i in range(bottom,top-1,-1):
            local.append(mat[i][left])
        left+=1
        
        res.append(local)
		
	# rotating the elements by k.
    for ele in res:
        l=len(ele)
        r=k%l
        ele[::]=ele[r:]+ele[:r]
    
	# Again storing in the matrix.    
    top = 0
    bottom = len(mat)-1
    left = 0
    right = len(mat[0])-1
    while left<right and top<bottom:
        local=res.pop(0)
        for i in range(left,right+1):
            mat[top][i] = local.pop(0)
        top+=1
		
        for i in range(top,bottom+1):
            mat[i][right] = local.pop(0)
        right-=1
		
        for i in range(right,left-1,-1):
            mat[bottom][i] = local.pop(0)
        bottom-=1
		
        for i in range(bottom,top-1,-1):
            mat[i][left] = local.pop(0)
        left+=1
        
    return mat