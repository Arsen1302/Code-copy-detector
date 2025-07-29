class Solution:
    def solution_1349_4(self, matrix: List[List[int]]) -> int:
        odd = False  # is there an odd number of negative values?
        s, m = 0, math.inf  # sum, min

        for row in matrix:
            for num in row:
                if num < 0:
                    odd = not odd
                    num = -num
                s += num
                m = min(m, num)
        
        return -2*m*odd + s