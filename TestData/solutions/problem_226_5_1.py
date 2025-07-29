class Solution:

    def solution_226_5_1(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        v_pac = set()
        v_atl = set()
        
        def solution_226_5_2(v_set, row, col, curr_height):
            if row < 0 or row >= m or \
                col < 0 or col >= n or \
                    (row,col) in v_set or \
                        curr_height > heights[row][col]:
                return
            v_set.add((row, col))

            curr_height = heights[row][col]
            solution_226_5_2(v_set, row + 1, col, curr_height)
            solution_226_5_2(v_set, row - 1, col, curr_height)
            solution_226_5_2(v_set, row, col + 1, curr_height)
            solution_226_5_2(v_set, row, col - 1, curr_height)

        # Approach is to start from both sides of 
        # the oceans and then reach each point that can be 
        # reached while maintaining the visited indices

        # Iterate over columns and start from both 0, m-1 rows
        for col in range(n):
            solution_226_5_2(v_pac, 0, col, heights[0][col]) # First row
            solution_226_5_2(v_atl, m - 1, col, heights[m-1][col]) # Last row

        # Iterate over rows and start from both 0, n-1 cols
        for row in range(m):
            solution_226_5_2(v_pac, row, 0, heights[row][0]) # First column
            solution_226_5_2(v_atl, row, n-1, heights[row][n-1]) # Last column

        # Co-ordinates which can reach both the oceans are the winners
        # so we take intersection
        result = v_atl.intersection(v_pac)

        return result