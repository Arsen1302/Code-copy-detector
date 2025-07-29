class Solution:
    def solution_1464_3(self, matrix: List[List[int]]) -> bool:
        # bitmask
        n = len(matrix)

        for i in range(n):
            row_bit, col_bit, bitmask = 1, 1, 1
            for j in range(n):
                row_bit ^= 1 << matrix[i][j]
                col_bit ^= 1 << matrix[j][i]
                bitmask |= 1 << j + 1

            if row_bit ^ bitmask or col_bit ^ bitmask:
                return False
        
        return True