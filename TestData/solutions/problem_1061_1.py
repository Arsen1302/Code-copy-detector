class Solution:
    def solution_1061_1(self, mat: List[List[int]]) -> int:
        """
        The primary diagonal is formed by the elements A00, A11, A22, A33.
        Condition for Primary Diagonal:
            The row-column condition is row = column.

        The secondary diagonal is formed by the elements A03, A12, A21, A30. 
        Condition for Secondary Diagonal:
            The row-column condition is row = numberOfRows - column -1.
        """
        s = 0
        l , mid = len(mat), len(mat)//2
        for i in range(l):
            s += mat[i][i] # primary diagonal
            s += mat[len(mat)-i-1][i] # secondary diagonal
        
        # If the mat is odd, then diagonal will coincide, so subtract the middle element
        if l%2 != 0:
            s -= mat[mid][mid]
        
        return s