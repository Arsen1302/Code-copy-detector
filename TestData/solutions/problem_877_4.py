class Solution:
    def solution_877_4(self, mat: List[List[int]]) -> List[List[int]]:
        lst = []
        n, m = len(mat), len(mat[0])
        
        # leftmost column
        for i in range(n):
            lst.append([i, 0])
        
        # rightmost row
        for i in range(m):
            lst.append([0, i])
        
        lst.pop(0)
        
        for x, y in lst:
            arr = []
            i, j = x, y
            
            # getting the diagonal elements
            while i < n and j < m:
                arr.append(mat[i][j])
                i, j = i+1, j+1
            
            arr.sort()  # sort the elements
            
            i, j = x, y
            # setting the element in sorted order
            while i < n and j < m:
                mat[i][j] = arr.pop(0)
                i, j = i+1, j+1
        
        return mat