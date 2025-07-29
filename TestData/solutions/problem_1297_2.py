class Solution:
    def solution_1297_2(self, mat: List[List[int]]) -> List[int]:
        left, right = 0, len(mat[0]) - 1
        
        while left <= right:
            midCol = (left + right)//2
            maxRow = 0
            
            for i in range(len(mat)):
                maxRow = i if mat[i][midCol] > mat[maxRow][midCol] else maxRow
                
            isLeftBig = midCol - 1 >= 0 and mat[maxRow][midCol - 1] > mat[maxRow][midCol]
            isRightBig = midCol + 1 <= len(mat[0]) and mat[maxRow][midCol + 1] > mat[maxRow][midCol]
            
            if not isLeftBig and not isRightBig:
                return [maxRow, midCol]
            
            elif isRightBig:
                left = midCol + 1
            
            else:
                right = midCol - 1
                
        return None