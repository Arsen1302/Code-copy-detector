class Solution:
    def solution_386_2_1(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        
        def solution_386_2_2(i, j):
            s = squares = 0
            top, bottom = max(0, i - 1), min(m, i + 2)
            left, right = max(0, j - 1), min(n, j + 2)

            for x in range(top, bottom):
                for y in range(left, right):
                    s += img[x][y]
                    squares += 1
            
            return s // squares
                       
        return [[solution_386_2_2(i, j) for j in range(n)] for i in range(m)]