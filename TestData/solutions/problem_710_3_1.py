class Solution:
    def solution_710_3_1(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        # create a r, c matrix given the rows &amp; cols
        # each element represents a list [r, c] where r is the row &amp; c the col
        # find find the distances of all cells from the center (append to res)
        # sort the result by solution_710_3_2 function
        # Time O(M + N) Space O(M + N)
        
        
        def solution_710_3_2(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        matrix = [[i, j] for i in range(rows) for j in range(cols)]
        center = [rCenter, cCenter]
        matrix.sort(key=lambda c: solution_710_3_2(c, center))
        
        return matrix